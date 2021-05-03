from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.message import Message
from django.http import HttpResponse
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
import django.contrib.sessions
from django.views import View
from django.contrib import messages
from store.models.product import Product



class Cart(View):
    def get(self , request):
        ids=(list(request.session.get('cart').keys()))
        products=Product.get_product_by_id(ids)
        print(products)
        return render(request, 'cart.html',{'products':products})
