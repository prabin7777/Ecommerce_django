from django import template
from django.template.defaultfilters import stringfilter
register=template.Library()


@register.filter(name='currency')
def currency(number):
   return "रु "+str(number)
