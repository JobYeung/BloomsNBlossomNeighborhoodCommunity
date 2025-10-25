from django.shortcuts import render
from products.models import Product
from florists.models import Florist
from products.choices import flower_style_choices,flower_type_choices,occasion_choices,seasonal_choices
from django.http import HttpResponse
import datetime
from django.utils.translation import gettext as _


def index(request):
    # Check if the welcome cookie exists
    if not request.COOKIES.get('has_seen_welcome'):
        print(9999)
        response = render(request, 'pages/home.html')
        # Set a cookie that expires in 15 seconds
        expires = datetime.datetime.now() + datetime.timedelta(seconds=15)
        response.set_cookie('has_seen_welcome', 'true', expires=expires)
        return response
    else:
        # Redirect to a different page or render a different template if already visited
        # return render(request, 'pages/home.html')  # Replace 'home.html' with your actual home     
        products = Product.objects.filter(is_published=True)[:3]
        context = {
            'products':products,
            'flower_style_choices':flower_style_choices,
            'flower_type_choices':flower_type_choices,
            'occasion_choices':occasion_choices,
            'seasonal_choices':seasonal_choices,
                }
        return render(request, 'pages/index.html',context)


def welcome(request):
    response = render(request, 'pages/home.html')
    # Set a cookie that expires in 15 seconds
    expires = datetime.datetime.now() + datetime.timedelta(seconds=15)
    response.set_cookie('has_seen_welcome', 'true', expires=expires)
    return response

def about(request):
    florists = Florist.objects.order_by('-hire_date')[:3]
    mvp_florists = Florist.objects.all().filter(is_mvp=True)
    context = {
        "florists":florists,
        "mvp_florists":mvp_florists,
    }

    print("Individual objects in QuerySet:")
    for obj in context:
        print(obj) 
    return render(request, 'pages/about.html',context)

def my_view(request):
    greeting = _("Hello, world!")
    return HttpResponse(greeting)


# def index(request):
#     products = Product.objects.filter(is_published=True)[:3]
#     context = {
#         'products':products,
#         'flower_style_choices':flower_style_choices,
#         'flower_type_choices':flower_type_choices,
#         'occasion_choices':occasion_choices,
#         'seasonal_choices':seasonal_choices,
#                }
#     return render(request, 'pages/index.html',context)