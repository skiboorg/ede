from django.contrib import admin
from .models import *

class FilesInline (admin.TabularInline):
    model = CallbackFiles
    can_delete = False
    readonly_fields = ('file',)
    max_num = 0
    extra = 0

class CallbackAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'name', 'phone', 'email', 'workName']
    # search_fields = ('',)
    # exclude = ['']
    inlines = (FilesInline,)
    ordering = ('created_at',)

    class Meta:
        model = Callback


admin.site.register(Callback, CallbackAdmin)
admin.site.register(CallbackOrder)