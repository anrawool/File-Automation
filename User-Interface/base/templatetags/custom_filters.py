from django import template

register = template.Library()

@register.filter
def increment_counter(counter):
    return counter + 1
