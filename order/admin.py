from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'workName']
    # search_fields = ('',)
    # exclude = ['']
    ordering = ('created_at',)
    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
