from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self,  phone, password, **extra_fields):

        if not phone:
            raise ValueError('Не указан телефон')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,  phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user( phone, password, **extra_fields)


class User(AbstractUser):

    username = None
    first_name = None
    last_name = None
    email = models.EmailField('Эл. почта', unique=True)
    name = models.CharField('Имя', max_length=255, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=50, blank=False, unique=True)
    comment = models.TextField('Комментарий виден только админу', blank=True, null=True)
    isAllowEmail = models.BooleanField('Согласен на рассылку', default=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()

class UserLog(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, verbose_name='Пользователь')
    action = models.CharField('Действие', max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - пользователь {} : {}'.format(self.created_at, self.user.name, self.action)

    class Meta:
        verbose_name = "Лог действий"
        verbose_name_plural = "Логи действий"



