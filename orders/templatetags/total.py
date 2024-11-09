from django import template
register=template.Library()
@register.simple_tag(name='total')
def totall(cart):
    total=0
    for x in cart.added_items.all():
        total+=(x.qty*x.product.price)
    return total   