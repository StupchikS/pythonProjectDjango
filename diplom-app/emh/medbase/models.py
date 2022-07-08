from django.db import models


class Personal(models.Model):
    stuff_name = models.CharField(max_length=150, verbose_name='должность')
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


class Patient(models.Model):
    patient_number = models.CharField(max_length=150, unique=True, verbose_name='номер пациента')
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    data_birthday = models.DateField(verbose_name='дата рождения')
    number_oms = models.CharField(max_length=40, verbose_name="номер полиса")
    adres = models.CharField(max_length=200, verbose_name='адрес проживания')
    phone = models.CharField(max_length=200, verbose_name='телефон')

    def __str__(self):
        return self.patient_number

    class Meta:
        verbose_name = "Пациента"
        verbose_name_plural = 'Пациенты'
        ordering = ['fio']


class MedWork(models.Model):
    patient_number = models.ForeignKey('Patient', on_delete=models.PROTECT, verbose_name='номер пациента')
    data_work = models.DateField(verbose_name='дата приема')
    content_work = models.TextField(max_length=1000, verbose_name='описание приема')
    recomend_work = models.CharField(max_length=200, verbose_name='рекомендации')

    def __str__(self):
        return str(self.patient_number) + ' ' + str(self.data_work)

    class Meta:
        verbose_name = "Прием"
        verbose_name_plural = 'Приемы'
        ordering = ['-data_work']


class Blood(models.Model):
    patient_number = models.ForeignKey('Patient', on_delete=models.PROTECT, verbose_name='номер пациента')
    data_work = models.DateField(verbose_name='дата приема анализа')
    belock = models.CharField(max_length=10, verbose_name='белок')
    hgb = models.CharField(max_length=10, verbose_name='ХГБ')
    sugar = models.CharField(max_length=10, verbose_name='сахар')
    text_blood = models.CharField(max_length=100, blank=True, verbose_name='описание')

    def __str__(self):
        return str(self.patient_number) + ' ' + str(self.data_work)

    class Meta:
        verbose_name = "Анализ крови"
        verbose_name_plural = 'Анализы крови'
        ordering = ['-data_work']


class Urea(models.Model):
    patient_number = models.ForeignKey('Patient', on_delete=models.PROTECT, verbose_name='номер пациента')
    data_work = models.DateField(verbose_name='дата приема анализа')
    belock = models.CharField(max_length=10, verbose_name='белок')
    sugar = models.CharField(max_length=10, verbose_name='сахар')
    mochevina = models.CharField(max_length=10, verbose_name='мочевина')
    text_urea = models.CharField(max_length=100, blank=True, verbose_name='описание')

    def __str__(self):
        return str(self.patient_number) + ' ' + str(self.data_work)

    class Meta:
        verbose_name = "Анализ мочи"
        verbose_name_plural = 'Анализы мочи'
        ordering = ['-data_work']