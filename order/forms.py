from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = (
            'user',
            'workName',
            'subject',
            'about',
            'volume',
            'deadLine',
            'file',
            'comment'
        )

class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = (
            'user',
            'order',
            'message',
        )