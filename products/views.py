from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    cart[product_id_str] = cart.get(product_id_str, 0) + 1
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('index')


def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0.0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            subtotal = product.price * quantity
            total_price += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })
        except Product.DoesNotExist:
            continue

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart_detail')


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        request.session.modified = True
    return redirect('cart_detail')


def cart_status(request):
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())
    return {'cart_total_items': total_items}