from django import template
from django.contrib.auth.decorators import login_required


register = template.Library()

@register.filter()
def currency(value):
   return f'{value} Р'

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()

