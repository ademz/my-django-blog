from django.contrib.sitemaps import Sitemap

from .models import Post


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Post.objects.published()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return obj.get_absolute_url()
