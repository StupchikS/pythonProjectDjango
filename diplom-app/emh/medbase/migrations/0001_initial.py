# Generated by Django 4.0.4 on 2022-06-30 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuff_name', models.CharField(max_length=50, verbose_name='должность')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('content', models.TextField(blank=True, verbose_name='описание')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото')),
                ('number_for', models.IntegerField(verbose_name='порядок следования на странице')),
            ],
            options={
                'verbose_name': 'Штат больницы',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['number_for'],
            },
        ),
    ]
