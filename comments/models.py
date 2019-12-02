from django.db import models
from service.models import ServiceName

class Comment(models.Model):
    service = models.ManyToManyField(ServiceName,blank=True,verbose_name='Отзыв к услугам')
    image_big = models.ImageField('Картинка отзыва большая 590 х 435 px', upload_to='comments', blank=False)
    image_small = models.ImageField('Картинка отзыва маленькая 265 х 145px', upload_to='comments', blank=False)
    writtenBy = models.CharField('От кого отзыв', max_length=75, blank=False, default='')
    title = models.CharField('Заголовок отзыва (50 символов)', max_length=50, blank=False)
    description = models.CharField('Короткое описание отзыва (75 символов)', max_length=75, blank=False)
    shortReview = models.CharField('Первая часть отзыва (180 символов)', max_length=180, blank=False)
    fullReview = models.TextField('Вторая часть отзыва, показывается при нажатии на ЧИТАТЬ ДАЛЕЕ', blank=False)

    def __str__(self):
        return 'Отзыв №{}'.format(self.id)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"