from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "EDELWEYS"
admin.site.site_title = "Edelweys администрирование"
admin.site.index_title = "Edelweys администрирование"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.urls')),
    path('callback/', include('callback.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
