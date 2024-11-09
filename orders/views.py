from django.shortcuts import render,redirect
from . models import Order,OrderedItem
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE,
    )
    context={'cart':cart_obj}
    return render(request, 'cart.html',context)
@login_required(login_url='account')
def addCart(request):
    if request.POST:
        user=request.user
        customer=user.customer
        qty=int(request.POST.get('qty'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE

        )
        product=Product.objects.get(pk=product_id)
        ordered_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
        )
        if created:
            ordered_item.qty=qty
            ordered_item.save()
        else:
            ordered_item.qty+=qty
            ordered_item.save()    
        return redirect('cart')
@login_required(login_url='account')
def remove(request,pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')
def checkout(request):
    try:
        if request.POST:
            user=request.user
            customer=user.customer
            total=float(request.POST.get('total'))
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message="Your order is succusfull, Your Item will deliver within 2 days"
                messages.success(request,status_message)
            else:
                status_message="Unable to process, add somthing to cart"
                messages.error(request,status_message)
    except:
        status_message="Unable to process, add somthing to cart"
        messages.error(request,status_message)
    return redirect('home')    
@login_required(login_url='account')
def showOrders(request):
    user=request.user
    customer=user.customer
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
    return render(request, 'order.html',context)