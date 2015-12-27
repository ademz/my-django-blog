from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from .views import PostListView, PostView, TagListView
from .feeds import BlogFeed
from .sitemaps import BlogSitemap

sitemaps = {
    "blog": BlogSitemap
}

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='home_page'),

    # feeds
    url(r'^feeds/$',  BlogFeed()),

    url(r'^(?P<slug>[-\w]+)/$', PostView.as_view(), name='post_detail'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagListView.as_view(), name='tag_list'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    # sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]
