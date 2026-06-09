from django.urls import path
from . import views

# /products
# /products/1/detail
# /products/new

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart')
]