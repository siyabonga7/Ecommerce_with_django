from django.shortcuts import render, get_object_or_404, render
from .models import product,Customer

# Create your views here.
def product_list(request):
    products = product.objects.all()
    context = {
        'products': products
    }
    return render(request,'Ecommerce/product_list.html',context)

def product_detail(request,pk):
    product = get_object_or_404(product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'Ecommerce/product_details.html', context)

def customer_list(request):
    customer = customer.objects.all()
    context ={
        'customers':customer
    }
    return render (request,'Ecommerce/customer_list.html', context)

def customer_detail(request,pk):
    customer = get_object_or_404
    context = {
        'customer': customer 
    }
    return render(request,'Ecommerce/customer_detail.html', context)