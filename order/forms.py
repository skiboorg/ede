from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = (
            'workName',
            'subject',
            'about',
            'volume',
            'deadLine',
            'file',
            'comment'
        )
