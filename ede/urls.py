from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from service.sitemaps import *
from django.contrib.sitemaps.views import sitemap

admin.site.site_header = "EDE74"
admin.site.site_title = "EDE74 администрирование"
admin.site.index_title = "EDE74 администрирование"

sitemaps = {
    'static': StaticViewSitemap,
    'services': ServicesSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('', include('service.urls')),
    path('callback/', include('callback.urls')),
    path('user/', include('customuser.urls')),
    path('order/', include('order.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
