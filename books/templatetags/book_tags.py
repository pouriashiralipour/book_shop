from django import template

register = template.Library()


# lower case
@register.filter
def to_lowercase(value):
    return value.lower()


# upper case
@register.filter
def to_uppercase(value):
    return value.upper()
