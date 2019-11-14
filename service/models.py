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
    tagH1 = models.CharField('Тег Н1 для страницы с услугой. Для вставки города используйте выражение %TOWN%,'
                             ' для склонения города %TOWN_ALIAS%. Например: Заказать в городе %TOWN% курсовую работу ',
                           max_length=255,
                           blank=False, null=True)
    title = models.CharField('Тег TITLE для страницы с услугой. Для вставки города используйте выражение %TOWN%, для склонения города %TOWN_ALIAS%',
                             max_length=255,
                             blank=False, null=True)
    description = models.CharField('Тег DESCRIPTION для страницы с услугой. Для вставки города используйте выражение %TOWN%, для склонения города %TOWN_ALIAS%',
                             max_length=255,
                             blank=False, null=True)
    keywords = models.TextField('Тег KEYWORDS для страницы с услугой. Для вставки города используйте выражение %TOWN%, для склонения города %TOWN_ALIAS%',
                             max_length=255,
                             blank=False, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.name_slug != slug:
            testSlug = ServiceName.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-'+''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(ServiceName, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/service/{self.name_slug}/'

    def __str__(self):
        return 'Вид работы : {}'.format(self.name)

    class Meta:
        verbose_name = "Вид работы"
        verbose_name_plural = "Виды работ"


