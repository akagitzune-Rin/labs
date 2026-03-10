from django.shortcuts import render
from .models import Article
# Create your views here.
def archive(request):
    """Отображает список всех статей"""
    posts = Article.objects.all()
    return render(request, 'articles/archive.html', {'posts': posts})