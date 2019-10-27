from django.contrib import admin
from .models import *

class MessagesInline (admin.TabularInline):
    model = Messages
    extra = 0

class FilesInline (admin.TabularInline):
    model = OrderFile
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'workName', 'fullPrice', 'prePay','deadLine']
    # search_fields = ('',)
    # exclude = ['']
    inlines = (FilesInline,MessagesInline,)
    list_filter = ('is_complete',)
    ordering = ('created_at',)
    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus)
