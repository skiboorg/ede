from django.contrib import admin
from .models import *

class ServiceNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'time']
    search_fields = ('name_lower',)
    exclude = ['name_slug', 'name_lower']

    class Meta:
        model = ServiceName

admin.site.register(ServiceName,ServiceNameAdmin)

class SeoTagAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('indexTitle',),
            'description': "This is a set of fields group into a fieldset."
        }),
    )
    class Meta:
        model = SeoTag


admin.site.register(SeoTag)