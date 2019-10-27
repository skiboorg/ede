from django.db import models

class Callback(models.Model):
    workName = models.CharField('Вид работы', max_length=255, blank=False)
    subject = models.CharField('Предмет', max_length=255, blank=False)
    about = models.CharField('Тема', max_length=255, blank=False)
    volume = models.IntegerField('Объем', blank=True, null=True)
    deadLine = models.CharField('Срок', max_length=255, blank=True, default='Пользователь не указал')
    name = models.CharField('Имя', max_length=255, blank=False, default='Нет данных')
    phone = models.CharField('Телефон', max_length=255, blank=False, default='Нет данных')
    email = models.EmailField('Email', max_length=255, blank=False, default='Нет данных')
    file = models.FileField('Загруженный файл', upload_to='callback_files', blank=True)
    created_at = models.DateTimeField('Дата заполнения', auto_now_add=True)

    def __str__(self):
        return 'Форма обратной связи. Заполнена {} '.format(self.created_at)

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"


class CallbackOrder(models.Model):
    userName = models.CharField('Имя',max_length=255, blank=False, default='Нет данных')
    userPhone = models.CharField('Телефон', max_length=255, blank=False, default='Нет данных')


    def __str__(self):
        return 'Форма заказа звонка. От {} '.format(self.userName)

    class Meta:
        verbose_name = "Форма заказа звонка"
        verbose_name_plural = "Формы заказа звонка"