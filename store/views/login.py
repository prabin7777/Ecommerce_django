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



class login(View):
    def get(self , request):
        return render(request, 'login.html')
    def post(self,request):
        name = request.POST.get('first_name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        costomor = Customer.get_customer_by_phone(phone)


        if costomor:
            passkey = Customer.get_customer_by_password(password)


            if passkey:
                successful = 'loged in successfully'
                request.session['customer']=phone
                request.session['Name']=name






                # request.session['customer_id'] =adress

                request.session['phone'] =phone
                request.session['id'] =id(self)
                request.session['name']=name

                return redirect('homepage')

            else:
                error='invalid try'
                return render(request, 'login.html', {'error': error})
        else:
            error='Phone number or password invalid !!'
            return render(request, 'login.html', {'error': error})

def logout(request):
    request.session.clear()
    return redirect('login')