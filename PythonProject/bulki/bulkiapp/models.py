from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    summary = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    author = models.ForeignKey(User, null=True, blank=True, verbose_name="Автор", on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='img/', verbose_name="Изображение", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    new = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Новость")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)
    text = models.TextField(verbose_name="Текст комментария")
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"