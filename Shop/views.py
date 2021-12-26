from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Image, Category
from django.template import loader, Context


def cats(request, id):
    products = Product.objects.filter(category_name=id)
    context = {'products': products}
    return render(request, 'Shop/Products.html', context)


def page_product(request, id):
    product = Product.objects.get(id=id)
    imgs_src = product.imgs
    context = {'product': product, 'imgs': imgs_src}
    return render(request, 'Shop/Product.html', context)


def page_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'Shop/Cats.html', context)