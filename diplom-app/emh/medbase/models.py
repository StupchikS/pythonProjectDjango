from django.db import models


class Personal(models.Model):
    stuff_name = models.CharField(max_length=50, verbose_name='должность')
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    content = models.TextField(blank=True, verbose_name="описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="фото")
    number_for = models.IntegerField(verbose_name="порядок следования на странице")

    def __str__(self):
        return self.stuff_name

    class Meta:
        verbose_name = "Штат больницы"
        verbose_name_plural = 'Сотрудники'
        ordering = ['number_for']

