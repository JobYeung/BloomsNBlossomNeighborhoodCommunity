from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import flower_style_choices,flower_type_choices,occasion_choices,seasonal_choices
from django.db.models import Q

def products(request):
    products = Product.objects.order_by('list_date').filter(is_published=True)
    #products = Product.objects.all()
    paginator=Paginator(products,3)
    page=request.GET.get('page')
    paged_product=paginator.get_page(page)
    context = {'products':paged_product}
    print(context)
    return render(request,'products/products.html',context)

def product(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product":product}
    print(context)
    return render(request,'products/product.html',context)

def search(request):
    queryset_list = Product.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(description__icontains=keywords)|Q(title__icontains=keywords)|Q(florist__name__icontains=keywords))
    if 'flower_type' in request.GET:
        flower_type = request.GET['flower_type']
        if flower_type:
            queryset_list = queryset_list.filter(flower_type__icontains=flower_type)
    if 'flower_style' in request.GET:
        flower_style = request.GET['flower_style']
        if flower_style:
            queryset_list = queryset_list.filter(flower_style__icontains=flower_style)
    if 'occasion' in request.GET:
        occasion = request.GET['occasion']
        if occasion:
            queryset_list = queryset_list.filter(occasion__icontains=occasion)
            #queryset_list = queryset_list
    if 'seasonal' in request.GET:
        seasonal = request.GET['seasonal']
        if seasonal:
            queryset_list = queryset_list.filter(seasonal__icontains=seasonal)
    paginator=Paginator(queryset_list,3)
    page=request.GET.get('page')
    paged_products=paginator.get_page(page)
    context = {
        'products':paged_products,
        'flower_type_choices':flower_type_choices,
        'flower_style_choices':flower_style_choices,
        'occasion_choices':occasion_choices,
        'seasonal_choices':seasonal_choices,
        'values':request.GET,
    }
    return render(request, 'products/search.html',context)

