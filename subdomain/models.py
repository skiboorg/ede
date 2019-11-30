from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from service.models import ServiceName

class Domain(models.Model):
    name = models.CharField('Поддомен маленькими буквами (например, msk)',max_length=30, blank=False, null=True)
    town = models.CharField('Город (например, Москва)',max_length=30, blank=False, null=True)
    townAlias = models.CharField('Склонение города (должно отвечать на вопрос ГДЕ, например, Москве)',
                                      max_length=30,
                                      blank=False,
                                      null=True)

    contactStreet = models.CharField('Индекс, Улица, Дом (например, 703410, ул. Ленана, 55)', max_length=100, blank=False)
    contactPhone = models.CharField('Номер телефона', max_length=100,
                                     blank=False,
                                     null=True)
    yandexTAG = models.CharField('Код подтверждения Яндекс', max_length=255, blank=True, null=True)
    googleTAG = models.CharField('Код подтверждения google', max_length=255, blank=True, null=True)


    def __str__(self):
        return 'Поддомен для города {}'.format(self.town)

    class Meta:
        verbose_name = "Поддомен"
        verbose_name_plural = "Поддомены"

class HomePageText(models.Model):
    domain = models.ForeignKey(Domain,blank=False,verbose_name='Для поддомена', null=True, on_delete=models.CASCADE, related_name='hometext')
    fullText = RichTextUploadingField('Текст для главной страницы. Для вставки города используйте выражение %TOWN%, для склонения города %TOWN_ALIAS%', blank=False, null=True)

    def __str__(self):
        return 'Текст на главной страницы для города {}'.format(self.domain.town)

    class Meta:
        verbose_name = "Текст на главной"
        verbose_name_plural = "Тексты на главной"


class ServicePageText(models.Model):
    domain = models.ForeignKey(Domain,blank=False,verbose_name='Для поддомена', null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceName,blank=False,verbose_name='Для услуги', null=True, on_delete=models.CASCADE)
    fullText = RichTextUploadingField('Текст для страницы услуги, Для вставки города используйте выражение %TOWN%, для склонения города %TOWN_ALIAS%', blank=False, null=True)

    def __str__(self):
        return 'Текст на страницы услуги {} для города {}'.format(self.service.name, self.domain.town)

    class Meta:
        verbose_name = "Текст на страницы услуги"
        verbose_name_plural = "Тексты на страниц услуг"