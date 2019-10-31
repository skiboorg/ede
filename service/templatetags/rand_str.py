from django import template
from random import choices
import base64
import string

register = template.Library()
@register.simple_tag
def random_str():
    return ''.join(choices(string.ascii_lowercase + string.digits, k=9))

@register.simple_tag
def random_str1(s):
    return base64.b64encode(bytes(str(s),'utf-8'))