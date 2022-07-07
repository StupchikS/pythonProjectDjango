# Generated by Django 4.0.4 on 2022-07-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_options_remove_blog_cat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='контент')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'Настройка главной страницы',
                'verbose_name_plural': 'Настройки главной страницы',
            },
        ),
    ]
