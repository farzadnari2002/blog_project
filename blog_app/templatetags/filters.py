from django import template



register = template.Library()


@register.filter('cut')
def cutter(value, arg):
    return value[:arg]+'...'

