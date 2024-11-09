from django import template
register=template.Library()
@register.filter(name='rows')
def rows(lst, row_size):
    for i in range(0, len(lst), row_size):
        yield lst[i:i + row_size]