from django import template

register = template.Library()


@register.filter('join_link')
def join_link(value, arg):
    from django.utils.html import conditional_escape
    links = []
    for obj in value:
        links.append('<a href="%s">%s</a>' % (
            obj.get_absolute_url(), conditional_escape(obj)
            ))

    return arg.join(links)
