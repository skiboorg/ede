from django import template
from random import choices
import string

register = template.Library()
@register.simple_tag
def random_str():
    return ''.join(choices(string.ascii_lowercase + string.digits, k=9))