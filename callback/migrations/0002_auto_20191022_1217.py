# Generated by Django 2.2.6 on 2019-10-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='volume',
            field=models.IntegerField(blank=True, null=True, verbose_name='Объем'),
        ),
    ]