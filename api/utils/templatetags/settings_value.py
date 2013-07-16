# -*- coding: utf-8 -*-
from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def settings_value(name):
    """
    Usage example:

    ::
        {% templatetag openblock %} settings_value "LANGUAGE_CODE" {% templatetag closeblock %}

    """
    return getattr(settings, name, "")
