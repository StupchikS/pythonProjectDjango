from django.db import models
from django.urls import reverse


class Blog(models.Model):  #  модель данных о новостях больницы
    title = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="урл")
    content = models.TextField(blank=True, verbose_name="контент")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="фото")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="дата публикации")
    time_update = models.DateTimeField(auto_now=True, verbose_name="дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'
        ordering = ['-time_created']


class Index(models.Model):  #  модель данных о больнице
    title = models.CharField(max_length=200, blank=True, verbose_name='Наименование больницы')
    content = models.TextField(verbose_name="контент")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="фото")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка главной страницы"
        verbose_name_plural = 'Настройки главной страницы'

