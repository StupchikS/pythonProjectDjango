# Generated by Django 4.0.4 on 2022-07-08 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medbase', '0003_alter_blood_text_blood_alter_urea_text_urea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_number',
            field=models.CharField(max_length=150, unique=True, verbose_name='номер пациента'),
        ),
    ]