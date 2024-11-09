from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_product=Product.objects.order_by('priority')[:4]
    latest_product=Product.objects.order_by('-id')[:4]
    context={
        'featured_product':featured_product,
        'latest_product':latest_product,
    }
    return render(request,'index.html',context)

def list_product(request):
    page=1
    if 'page' in request.GET:
        page=request.GET['page']
    product_list=Product.objects.order_by('priority')
    pagination=Paginator(product_list,8)
    product_list=pagination.get_page(page)
    context={'products':product_list}
    return render(request,'product.html',context)
def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render(request,'product_detail.html',context)