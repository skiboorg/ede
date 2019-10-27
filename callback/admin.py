from django.contrib import admin
from .models import *


class CallbackAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'name', 'phone', 'email', 'workName']
    # search_fields = ('',)
    # exclude = ['']
    ordering = ('created_at',)
    class Meta:
        model = Callback


admin.site.register(Callback, CallbackAdmin)
admin.site.register(CallbackOrder)