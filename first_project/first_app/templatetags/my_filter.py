from django import template

register = template.Library()

def my_filter(value, arg):
    return value.replace(arg, '')


register.filter('my_filter', my_filter)