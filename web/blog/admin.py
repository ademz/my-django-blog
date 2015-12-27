from django.contrib import admin
from django.utils.translation import ugettext_lazy

from .models import Post, Tag, Category


class MyAdminSite(admin.AdminSite):
    site_title = ugettext_lazy('My Blog Administration')
    site_header = ugettext_lazy('My Blog Administration')
    index_title = ugettext_lazy('Blog Admin')


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created')

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['author'] = request.user
        request.GET = data
        return super(PostAdmin, self).add_view(request,
                                               form_url="",
                                               extra_context=extra_context)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

admin.site = MyAdminSite()
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
