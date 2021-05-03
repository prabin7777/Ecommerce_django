from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.message import Message
# from django.http import HttpResponse
# from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
# from django.views import View
from django.views import View

name="unknown"
# Create your views here.
class Index(View):
    def post(self, request):
        (product)=str(request.POST.get('product_id'))
        remove=(request.POST.get('remove'))
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            # print(str(quantity) + 'yo ho ni ta')



            if quantity:
                if remove:
                     if quantity==1:
                         cart.pop(product)
                     else:
                        cart[product]=quantity-1
                else:
                    cart[product] = quantity + 1

            else:

                cart[product] = 1

        else:
            cart={}
            cart[product] = 1


        request.session['cart'] =cart

        return redirect("homepage")


    def get(self, request):

        products = None
        cart=request.session.get("cart")
        if not cart:
            request.session.cart={}
        categories = Category.get_all_categories()
        messages = Message.get_all_message()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_id(categoryID)
        else:
            products = Product.get_all_products()
        welcome = str(request.session.get('name'))
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['messages'] = messages
        data['name'] = name
        data['welcome'] = welcome
        print("your pnone is " + str(request.session.get("phone")))
        print("your id is " + str(request.session.get("id")))
        print("your id is " + str(request.session.get("name")))

        return render(request, 'home.html', data)
class Recycle(View):
    def get(self, request):
        messages = Message.get_all_message()
        return render(request, 'recycling.html', {'messages': messages})


#
