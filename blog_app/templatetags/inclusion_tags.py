from django import template


register = template.Library()

@register.inclusion_tag('blog_app/test_for_inclusion.html')
def show_hello(name):
    return {'name':name}
