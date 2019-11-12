from django.forms import ModelForm

from .models import *


class CallbackForm(ModelForm):
    class Meta:
        model = Callback
        fields = (
            'workName',
            'subject',
            'about',
            'volume',
            'deadLine',
            'name',
            'phone',
            'email',

        )

class CallbackOrderForm(ModelForm):
    class Meta:
        model = CallbackOrder
        fields = (
            'userName',
            'userPhone',
        )
