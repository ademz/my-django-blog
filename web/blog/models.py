from __future__ import unicode_literals

from django.conf import settings
from django.contrib.sitemaps import ping_google
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_list', kwargs={'slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = RichTextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, null=True)
    author = models.ForeignKey(AUTH_USER_MODEL, related_name='added_posts')

    objects = PostQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.id is None and self.slug is None:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            # HTTP-related exceptions
            pass

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["-created"]
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
