from django.contrib import admin
from .models import *

class ServiceNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'time']
    search_fields = ('name_lower',)
    exclude = ['name_slug', 'name_lower']

    class Meta:
        model = ServiceName

admin.site.register(ServiceName,ServiceNameAdmin)
