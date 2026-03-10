from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article


def archive(request):
    """Отображает список всех статей"""
    posts = Article.objects.all()
    return render(request, 'articles/archive.html', {'posts': posts})

def get_article(request, article_id):
   
    # get_object_or_404 автоматически выбрасывает Http404, если объект не найден
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article.html', {'article': article})

@login_required(login_url='/admin/')
def create_post(request):
    """
    Создание новой статьи.
    Требует авторизации пользователя.
    """
    errors = []
    
    if request.method == 'POST':
        # Получаем данные из формы
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        text = request.POST.get('text', '').strip()
        
        # Валидация полей
        if not title:
            errors.append('Заголовок обязателен для заполнения.')
        
        if not text:
            errors.append('Текст статьи обязателен для заполнения.')
        
        if not author:
            errors.append('Автор обязателен для заполнения.')
        
        # Проверка уникальности заголовка
        if title and Article.objects.filter(title=title).exists():
            errors.append('Статья с таким заголовком уже существует.')
        
        # Если ошибок нет - сохраняем статью
        if not errors:
            article = Article.objects.create(
                title=title,
                author=author,
                text=text
            )
            messages.success(request, f'Статья "{title}" успешно создана!')
            return redirect('article', article_id=article.id)
    
    return render(request, 'articles/create_post.html', {'errors': errors})

# Добавлена новая часть кода
def login_user(request):
    """
    Авторизация пользователя.
    Обрабатывает GET (показ формы) и POST (проверка данных).
    """
    errors = []
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        # Валидация полей
        if not username:
            errors.append('Введите имя пользователя.')
        if not password:
            errors.append('Введите пароль.')
        
        # Проверка учётных данных
        if not errors:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {user.username}!')
                return redirect('archive')
            else:
                errors.append('Неверное имя пользователя или пароль.')
    
    return render(request, 'articles/login.html', {'errors': errors})


def logout_user(request):
    """
    Выход пользователя.
    Завершает сессию и перенаправляет на главную страницу.
    """
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('archive')


def register_user(request):
    """
    Регистрация нового пользователя.
    Проверяет уникальность username и заполненность полей.
    """
    errors = []
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        password_confirm = request.POST.get('password_confirm', '').strip()
        email = request.POST.get('email', '').strip()
        
        # Валидация полей
        if not username:
            errors.append('Имя пользователя обязательно.')
        if not password:
            errors.append('Пароль обязателен.')
        if password != password_confirm:
            errors.append('Пароли не совпадают.')
        if len(password) < 8:
            errors.append('Пароль должен быть не менее 8 символов.')
        
        # Проверка уникальности username
        if username and User.objects.filter(username=username).exists():
            errors.append('Пользователь с таким именем уже существует.')
        
        # Создание пользователя
        if not errors:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, f'Пользователь {username} успешно зарегистрирован!')
            return redirect('login')
    
    return render(request, 'articles/register.html', {'errors': errors})