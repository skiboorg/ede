from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *
from blog.models import BlogPost

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['prices']

    def location(self, item):
        return reverse(item)


class ServicesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return ServiceName.objects.all()


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.created_at

