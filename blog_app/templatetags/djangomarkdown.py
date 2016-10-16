# coding: utf-8

from markdown import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def djangomarkdown(value):
    return mark_safe(markdown(force_unicode(value), extras=["code-friendly"]))
