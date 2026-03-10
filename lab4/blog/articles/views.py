from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.
def archive(request):
    """Отображает список всех статей"""
    posts = Article.objects.all()
    return render(request, 'articles/archive.html', {'posts': posts})

def get_article(request, article_id):
    """
    Отображает одну статью по её ID.
    Если статья не найдена — возвращает ошибку 404.
    """
    # get_object_or_404 автоматически выбрасывает Http404, если объект не найден
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article.html', {'article': article})