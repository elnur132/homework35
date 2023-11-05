from django import template

register = template.Library()

@register.filter(name='replace_comma')
def intspace(value):
    return value * 2
