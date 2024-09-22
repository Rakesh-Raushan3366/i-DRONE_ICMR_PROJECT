from django import template
import re

register = template.Library()

@register.filter(name='numeric_value')
def numeric_value(value):
    # Extract numeric part from the value
    numeric_part = re.sub(r'[^\d]', '', value)
    return int(numeric_part) if numeric_part else 0