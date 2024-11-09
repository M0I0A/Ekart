from django.db import models
from customers.models import Customer
from products.models import Product
# Create your models here.
class Order(models.Model):
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    total_price=models.IntegerField(null=True)
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_CONFIRMED,'Order Confirmed'),(ORDER_PROCESSED,'Order Processed'),(ORDER_DELIVERED,'Order Delivered'),(ORDER_REJECTED,'Order Rejected'))
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)

    def __str__(self) -> str:
        return "Order-{}-{}".format(self.id,self.owner.name)


class OrderedItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name="added_cart")
    qty=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

    def __str__(self) -> str:
        return "Order_item-{}-Order-{}-{}-{}".format(self.id,self.owner.owner.id,self.owner.owner.name,self.product.title)
