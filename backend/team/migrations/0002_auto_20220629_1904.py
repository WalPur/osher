# Generated by Django 3.1.14 on 2022-06-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammate',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='teammate',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='teammate',
            name='position_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='teammate',
            name='position_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Должность'),
        ),
    ]
