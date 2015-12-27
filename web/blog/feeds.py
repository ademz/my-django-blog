from django.contrib.syndication.views import Feed

from .models import Post


class BlogFeed(Feed):
    title = "My posts"
    link = "/"
    description = "My post feeds"

    def items(self):
        return Post.objects.published()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
