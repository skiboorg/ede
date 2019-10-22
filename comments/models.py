from django.db import models

class Comment(models.Model):
    image = models.ImageField('Картинка отзыва', upload_to='comments', blank=False)
    title = models.CharField('Заголовок отзыва (50 символов)', max_length=50, blank=False)
    description = models.CharField('Короткое описание отзыва (75 символов)', max_length=75, blank=False)
    shortReview = models.CharField('Первая часть отзыва (180 символов)', max_length=180, blank=False)
    fullReview = models.TextField('Вторая часть отзыва, показывается при нажатии на ЧИТАТЬ ДАЛЕЕ', blank=False)

    def __str__(self):
        return 'Отзыв №{}'.format(self.id)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"