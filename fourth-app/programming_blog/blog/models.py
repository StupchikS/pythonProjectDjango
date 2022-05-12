from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="урл")
    content = models.TextField(blank=True, verbose_name="контент")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="фото")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="дата публикации")
    time_update = models.DateTimeField(auto_now=True, verbose_name="дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'
        ordering = ['-time_created']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
