from django import template
register=template.Library()
@register.simple_tag(name='tax')
def tax(total,taxP):
    return total*(taxP/100)