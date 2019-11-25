from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from random import choices
import string

class ServiceName(models.Model):
    name = models.CharField('Вид работы', max_length=255, blank=False, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    price = models.IntegerField('Цена на услугу', blank=False)
    time = models.CharField('Срок выполнения, например 14 дней',max_length=20, blank=False)
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
    defaultText = RichTextUploadingField('Текст для вставки на страницу услуги, если не указан иной', blank=True, null=True, default='Заполните это поле')
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


class SeoTag(models.Model):
    indexTitle = models.CharField('Тег Title для главной', max_length=255, blank=True, null=True)
    indexDescription = models.CharField('Тег Description для главной', max_length=255, blank=True, null=True)
    indexKeywords = models.TextField('Тег Keywords для главной',  blank=True, null=True)
    servicesTitle = models.CharField('Тег Title для страницы со всеми услугами', max_length=255, blank=True, null=True)
    servicesDescription = models.CharField('Тег Description для страницы со всеми услугам', max_length=255, blank=True, null=True)
    servicesKeywords = models.TextField('Тег Keywords для страницы со всеми услугам', blank=True, null=True)
    postsTitle = models.CharField('Тег Title для страницы со всеми статьями', max_length=255, blank=True, null=True)
    postsDescription = models.CharField('Тег Description для страницы со всеми статьями', max_length=255, blank=True,
                                           null=True)
    postsKeywords = models.TextField('Тег Keywords для страницы со всеми статьями', blank=True, null=True)
    contactTitle = models.CharField('Тег Title для страницы контакты', max_length=255, blank=True, null=True)
    contactDescription = models.CharField('Тег Description для страницы контакты', max_length=255, blank=True,
                                        null=True)
    contactKeywords = models.TextField('Тег Keywords для страницы контакты', blank=True, null=True)

    homeDefaultText = RichTextUploadingField('Текст для главной страницы, если не указан иной', blank=True, null=True, default='Заполните это поле')

    def __str__(self):
        return 'Теги для статических страниц'

    class Meta:
        verbose_name = "Теги для статических страниц"
        verbose_name_plural = "Теги для статических страниц"