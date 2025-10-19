from django.shortcuts import render
from products.models import Product
from florists.models import Florist
from products.choices import flower_style_choices,flower_type_choices,occasion_choices,seasonal_choices

def index(request):
    products = Product.objects.filter(is_published=True)[:3]
    context = {
        'products':products,
        'flower_style_choices':flower_style_choices,
        'flower_type_choices':flower_type_choices,
        'occasion_choices':occasion_choices,
        'seasonal_choices':seasonal_choices,
               }
    return render(request, 'pages/index.html',context)

def about(request):
    florists = Florist.objects.order_by('-hire_date')[:3]
    mvp_florists = Florist.objects.all().filter(is_mvp=True)
    context = {
        "florists":florists,
        "mvp_florists":mvp_florists,
    }
    return render(request, 'pages/about.html',context)