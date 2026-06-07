from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
# /products -> index
# uniform resource locator (address)

def index(request):
    products = Product.objects.all() # filter, get, save
    # return HttpResponse('hello, world. this is the products index.')
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('new products')