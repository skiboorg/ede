from django.db import models
from service.models import ServiceName

class Domain(models.Model):
    name = models.CharField('Поддомен маленькими буквами (например, msk)',max_length=30, blank=False, null=True)
    town = models.CharField('Город (например, Москва)',max_length=30, blank=False, null=True)
    townAliasWhere = models.CharField('Склонение города (должно отвечать на вопрос ГДЕ, например, Москве)',
                                      max_length=30,
                                      blank=False,
                                      null=True)
    townAliasFrom = models.CharField('Склонение города (должно отвечать на вопрос ОТКУДА, например, Москвы)',
                                     max_length=30,
                                     blank=False,
                                     null=True)
    contactStreet = models.CharField('Индекс, Улица, Дом (например, 703410, ул. Ленана, 55)', max_length=100, blank=False)
    contactPhone = models.CharField('Номер телефона', max_length=100,
                                     blank=False,
                                     null=True)

    def __str__(self):
        return 'Поддомен для города {}'.format(self.town)

    class Meta:
        verbose_name = "Поддомен"
        verbose_name_plural = "Поддомены"

class HomePageText(models.Model):
    domain = models.ForeignKey(Domain,blank=False,verbose_name='Для поддомена', null=True, on_delete=models.CASCADE)
    shortText = models.CharField('Короткий текст (200 символов)', max_length=200,
                                     blank=False,
                                     null=True)
    fullText = models.TextField('Текст для главной страницы', blank=False, null=True)

    def __str__(self):
        return 'Текст для главной страницы для города {}'.format(self.domain.town)

    class Meta:
        verbose_name = "Текст для главной"
        verbose_name_plural = "Тексты для главной"


class ServicePageText(models.Model):
    domain = models.ForeignKey(Domain,blank=False,verbose_name='Для поддомена', null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceName,blank=False,verbose_name='Для услуги', null=True, on_delete=models.CASCADE)
    shortText = models.CharField('Короткий текст (200 символов)', max_length=200,
                                 blank=False,
                                 null=True)
    fullText = models.TextField('Текст для страницы услуги', blank=False, null=True)

    def __str__(self):
        return 'Текст для страницы услуги {} для города {}'.format(self.service.name, self.domain.town)

    class Meta:
        verbose_name = "Текст для страницы услуги"
        verbose_name_plural = "Тексты для страниц услуг"