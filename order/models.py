from django.db import models
from django.db.models.signals import post_save, post_delete

from customuser.models import User


class Order(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, verbose_name='Пользователь')
    workName = models.CharField('Вид работы', max_length=255, blank=False)
    subject = models.CharField('Предмет', max_length=255, blank=False)
    about = models.CharField('Тема', max_length=255, blank=False)
    volume = models.IntegerField('Объем', blank=True, null=True)
    deadLine = models.CharField('Срок', max_length=255, blank=True, default='Пользователь не указал')

    fullPrice = models.IntegerField('Полная стоимость', default=0)
    prePay = models.IntegerField('Предоплата', default=0)
    status = models.CharField('Статус заказа', max_length=255, blank=True, default='Поступил в обработку. Идет расчет цены')
    created_at = models.DateTimeField('Дата заказа', auto_now_add=True)
    complete = models.IntegerField('Процент готовности (отображается в ЛК)', default=0)
    is_complete = models.BooleanField('Заказ выполнен ?', default=False)
    is_fullPayed = models.BooleanField('Оплачен полностью ?', default=False)
    is_prePayed = models.BooleanField('Внесена предоплата?', default=False)
    comment = models.TextField('Комментарий к заказу от пользователя', blank=True, default='')
    admin_comment = models.TextField('Комментарий к заказу (виден только админу)', blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.is_complete:
            if self.fullPrice:
                self.status = 'Стоимость расчитана, ожидаем предоплату'
                self.complete = 10
            if self.is_prePayed:
                self.status = 'Предоплата получена'
                self.complete = 25
            if self.is_fullPayed:
                self.is_prePayed = True
                self.status = 'Заказ оплачен'
                self.complete = 50

        if self.fullPrice:
            self.prePay = round(self.fullPrice / 2)
        self.deadLine = '.'.join(self.deadLine.split('-')[::-1])
        super(Order, self).save(*args, **kwargs)

    def __str__(self):

        return 'Заказ №{}'.format(self.id)


    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class OrderFile(models.Model):
    order = models.ForeignKey(Order, blank=False, on_delete=models.CASCADE, verbose_name='К заказу', related_name='orderfile')
    comment = models.TextField('Комментарий к файлу (виден пользователю)', blank=True, default='')
    file = models.FileField('Файл', upload_to='order_files', blank=False, null=True)

    def __str__(self):
        return 'Выполненная работа к заказу №{} '.format(self.order.id)

    class Meta:
        verbose_name = "Файл выполненной работы"
        verbose_name_plural = "Выполненные работы"

class OrderFiles(models.Model):
    order = models.ForeignKey(Order,blank=False,null=False,on_delete=models.CASCADE)
    file = models.FileField('Загруженный файл', upload_to='new_order_files', blank=True)

    def __str__(self):
        return 'Прикрепленный файл к заказу {} '.format(self.order.id)

    class Meta:
        verbose_name = "Прикрепленный файл к заказу"
        verbose_name_plural = "Прикрепленные файлы к заказу"

class Messages(models.Model):
    order = models.ForeignKey(Order, blank=False, on_delete=models.CASCADE, verbose_name='Сообщение к заказу', related_name='ordermessages')
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, verbose_name='От пользователя')
    message = models.TextField('Сообщение', default='')
    reply = models.TextField('Ответ', blank=True)
    created_at = models.DateTimeField('Дата создания сообщения', auto_now_add=True)
    updated_at = models.DateTimeField('Дата ответа',auto_now=True)

    def __str__(self):
        return 'Сообщение к заказу №{} '.format(self.order.id)

    class Meta:
        verbose_name = "Сообщение к заказу"
        verbose_name_plural = "Сообщения к заказам"


def Order_post_save(sender,instance,**kwargs):
    print('Order_post_save')
    instance.order.status = 'Заказ выполнен'
    instance.order.complete = 100
    instance.order.is_complete = True
    instance.order.save(force_update=True)
    print(instance.order.complete)
    print(instance.order.status)
    print(instance.order.is_complete)

def Order_post_delete(sender, instance, **kwargs):
    print('Order_post_del')
    instance.order.status = 'Заказ оплачен'
    instance.order.complete = 50
    instance.order.is_complete = False
    instance.order.save(force_update=True)
    print(instance.order.complete)
    print(instance.order.status)
    print(instance.order.is_complete)

post_delete.connect(Order_post_delete, sender=OrderFile)
post_save.connect(Order_post_save, sender=OrderFile)


class Payment(models.Model):
    order = models.ForeignKey(Order,blank=True,null=True,on_delete=models.CASCADE, verbose_name='Платеж к заказу')
    user = models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE, verbose_name='Платеж от')
    type = models.CharField('Тип платежа', max_length=255, blank=True)
    sender = models.CharField('Номер счета отправителя', max_length=255, blank=True)
    amount = models.CharField('Зачислено на счет', max_length=255, blank=True)
    withdraw_amount = models.CharField('Списано с плательщика', max_length=255, blank=True)
    operation_id = models.CharField('Номер операции на строне ЯндексДенег', max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} к заказу {} от {}, сумма {}, дата {}'.format(self.type, self.order.id,self.user.phone,self.amount,self.created_at)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"