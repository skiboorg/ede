# Generated by Django 2.2.6 on 2019-11-12 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='Поддомен маленькими буквами (например, msk)')),
                ('town', models.CharField(max_length=30, null=True, verbose_name='Город (например, Москва)')),
                ('townAliasWhere', models.CharField(max_length=30, null=True, verbose_name='Склонение города (должно отвечать на вопрос ГДЕ, например, Москве)')),
                ('townAliasFrom', models.CharField(max_length=30, null=True, verbose_name='Склонение города (должно отвечать на вопрос ОТКУДА, например, Москвы)')),
                ('contactStreet', models.CharField(max_length=100, verbose_name='Индекс, Улица, Дом (например, 703410, ул. Ленана, 55)')),
                ('contactPhone', models.CharField(max_length=100, null=True, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Поддомен',
                'verbose_name_plural': 'Поддомены',
            },
        ),
        migrations.CreateModel(
            name='ServicePageText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortText', models.CharField(max_length=200, null=True, verbose_name='Короткий текст (200 символов)')),
                ('fullText', models.TextField(null=True, verbose_name='Текст для страницы услуги')),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subdomain.Domain', verbose_name='Для поддомена')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.ServiceName', verbose_name='Для услуги')),
            ],
            options={
                'verbose_name': 'Текст для страницы услуги',
                'verbose_name_plural': 'Тексты для страниц услуг',
            },
        ),
        migrations.CreateModel(
            name='HomePageText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortText', models.CharField(max_length=200, null=True, verbose_name='Короткий текст (200 символов)')),
                ('fullText', models.TextField(null=True, verbose_name='Текст для главной страницы')),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subdomain.Domain', verbose_name='Для поддомена')),
            ],
            options={
                'verbose_name': 'Текст для главной',
                'verbose_name_plural': 'Тексты для главной',
            },
        ),
    ]
