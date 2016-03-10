from django.contrib.syndication.views import Feed
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Post, Tag


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    queryset = Post.objects.published()
    context_object_name = 'posts'
    paginate_by = 10


class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.published()


class TagListView(ListView):
    model = Post
    template_name = 'tag_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        if not hasattr(self, 'tag'):
            raise Http404
        context['tag'] = self.tag.name
        return context

    def get_queryset(self):
        try:
            self.tag = Tag.objects.get(slug=self.kwargs['slug'])
        except ObjectDoesNotExist:
            return None

        return Post.objects.published().filter(tags__in=[self.tag])
