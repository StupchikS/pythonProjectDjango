# Generated by Django 4.0.4 on 2022-07-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medbase', '0002_patient_alter_personal_stuff_name_urea_medwork_blood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood',
            name='text_blood',
            field=models.CharField(blank=True, max_length=100, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='urea',
            name='text_urea',
            field=models.CharField(blank=True, max_length=100, verbose_name='описание'),
        ),
    ]
