# Generated by Django 2.2.6 on 2019-11-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20191125_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='seotag',
            name='fbPixel',
            field=models.TextField(blank=True, null=True, verbose_name='Код пикселя'),
        ),
        migrations.AddField(
            model_name='seotag',
            name='yandexMetrika',
            field=models.TextField(blank=True, null=True, verbose_name='Код Яндекс метрики'),
        ),
    ]