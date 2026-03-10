from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    author = models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст статьи")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):        #метод, который определяет, как объект будет представляться в виде строки
        return self.title
    
    def get_excerpt(self):    #текст>50=..., текст<50=вся статья
        """Возвращает первые 50 символов текста статьи"""
        return self.text[:50] + '...' if len(self.text) > 50 else self.text
    
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"  
        ordering = ['-created_date'] 