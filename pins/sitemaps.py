











from django.contrib.sitemaps import Sitemap

from .models import Pin


class PinSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Pin.objects.all()

    def lastmod(self, obj):
        return obj.date_created


#class ProfileSitemap(Sitemap):
    #changefreq = "weekly"
    #priority = 0.9

    #def items(self):
        #return Profile.objects.all()

    #def lastmod(self, obj):
        #return obj.created_on

    # def location(self, item):
    #     return reverse(item)
