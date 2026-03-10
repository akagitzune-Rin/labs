from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article

# Create your views here.
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