from django import template

register = template.Library()

@register.tag
def hello_world():
    salute = 'Hello'
    
    return salute