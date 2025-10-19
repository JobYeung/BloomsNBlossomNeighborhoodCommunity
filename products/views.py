from django.shortcuts import render
from .models import Product

def products(request):
    products = Product.objects.all
    context = {'products':products}
    return render(request,'products/products.html',context)

def product(request):
    return render(request, 'proucts/product.html')

def search(request):
    return render(request, 'products/search.html')

