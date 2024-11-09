from django import template
register=template.Library()
@register.simple_tag(name='get_status')
def get_status(status):
    d={1:'Confirmed',2:'Processed',3:'Delivered',4:'Rejected'}
    return d[status]