from django.db import models


class StatusCrm(models.Model):  # статус заявки
    status_name = models.CharField(max_length=200, verbose_name='Название статуса обращения')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус обращения'
        verbose_name_plural = 'Статусы обращений'


class Order(models.Model):  # Заказы
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.IntegerField(max_length=11, verbose_name='Телефон')
    order_email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Электронная почта')
    order_context = models.CharField(max_length=500, null=True, blank=True, verbose_name='Сообщение')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'


class CommentsCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст коментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата коментария')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
