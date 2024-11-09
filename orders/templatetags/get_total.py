from django import template
register=template.Library()
@register.simple_tag(name='get_total')
def get_total(total,tax):
    return total+tax