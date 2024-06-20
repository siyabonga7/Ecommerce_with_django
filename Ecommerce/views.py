from django.shortcuts import render
from .models import product

# Create your views here.
def product_list(request):
    products = product.objects.all()
    context = {
        'products': products
    }
    return render(request,'Ecommerce/product_list.html',context)