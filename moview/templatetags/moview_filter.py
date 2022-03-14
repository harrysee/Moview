from django import template

register = template.Library()

@register.filter(name='index_i')
def index_i(l, i):
    try:
        return l[i]
    except:
        return None