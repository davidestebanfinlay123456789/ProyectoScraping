from django import template

register = template.Library()

@register.filter
def split_author(value):
    # Divide la cadena en una lista de autores
    return value.split(', ')