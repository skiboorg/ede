from django.db import models
from customuser.models import User

class Order(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, verbose_name='Пользователь')
    workName = models.CharField('Вид работы', max_length=255, blank=False)
    subject = models.CharField('Предмет', max_length=255, blank=False)
    about = models.CharField('Тема', max_length=255, blank=False)
    volume = models.IntegerField('Объем', blank=True, null=True)
    deadLine = models.CharField('Срок', max_length=255, blank=True, default='Пользователь не указал')
    file = models.FileField('Загруженный файл', upload_to='callback_files', blank=True)
    fullPrice = models.IntegerField('Полная стоимость', default=0)
    prePay = models.IntegerField('Предоплата', default=0)
    created_at = models.DateTimeField('Дата заказа', auto_now_add=True)
    is_complete = models.BooleanField('Заказ выполнен ?', default=False)
    complete = models.IntegerField('Процент готовности (отображается в ЛК)', default=0)
    comment = models.TextField('Комментарий к заказу от пользователя', blank=True, default='')
    admin_comment = models.TextField('Комментарий к заказу (виден только админу)', blank=True, default='')

    def __str__(self):
        return 'Заказ №{} '.format(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class OrderFile(models.Model):
    order = models.ForeignKey(Order, blank=False, on_delete=models.CASCADE, verbose_name='К заказу')
    comment = models.TextField('Комментарий к файлу (виден пользователю)', blank=True, default='')
    file = models.FileField('Файл', upload_to='order_files', blank=False, null=True)

    def __str__(self):
        return 'Файл к заказу №{} '.format(self.order.id)

    class Meta:
        verbose_name = "Файл к заказу"
        verbose_name_plural = "Файлы к заказам"