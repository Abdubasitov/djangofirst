from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    title = models.CharField("Название категории", max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class News(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='news'
    )
    title = models.CharField("Заголовок", max_length=500)
    image = models.ImageField(upload_to='newsMedia', blank=True, null=True)
    description = CKEditor5Field("Описание", config_name='extends')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-id']
