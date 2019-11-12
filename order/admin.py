from django.contrib import admin
from .models import *

class MessagesInline (admin.TabularInline):
    model = Messages
    extra = 0

class FilesInline (admin.TabularInline):
    model = OrderFile
    extra = 0

class UploadedFilesInline (admin.TabularInline):
    model = OrderFiles
    can_delete = False
    readonly_fields = ('file',)
    max_num = 0
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'workName', 'fullPrice', 'prePay','deadLine','is_fullPayed','is_prePayed']
    # search_fields = ('',)
    #exclude = []
    inlines = (UploadedFilesInline, MessagesInline, FilesInline)
    list_filter = ('is_complete','is_fullPayed','is_prePayed',)
    ordering = ('created_at',)
    readonly_fields = ['status','complete','prePay','is_complete','is_fullPayed','is_prePayed']
    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)

