from django.db import models
from pytils.translit import slugify
from random import choices
import string

class ServiceName(models.Model):
    name = models.CharField('Вид работы', max_length=255, blank=False, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    price = models.IntegerField('Цена на услугу', blank=False)
    time = models.IntegerField('Срок в днях', blank=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        testSlug = ServiceName.objects.filter(name_slug=slug)
        slugRandom = ''
        if testSlug:
            slugRandom = '-'+''.join(choices(string.ascii_lowercase + string.digits, k=2))
        self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(ServiceName, self).save(*args, **kwargs)

    def __str__(self):
        return 'Вид работы : {}'.format(self.name)

    class Meta:
        verbose_name = "Вид работы"
        verbose_name_plural = "Виды работ"


class Subject(models.Model):
    name = models.CharField('Предмет', max_length=255, blank=False, null=True)

    def __str__(self):
        return 'Предмет : {}'.format(self.name)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
