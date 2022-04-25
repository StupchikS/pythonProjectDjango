# Generated by Django 4.0.4 on 2022-04-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricCarDir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='electric_car_dir/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
