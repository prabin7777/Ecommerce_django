
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.message import Message
from django.http import HttpResponse
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password

from django.views import View


class sinup(View):
    def get(self,request):
        return render(request, 'sinup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        adress = postData.get('adress')
        # validation
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'adress': adress

        }
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            adress=adress)

        error = validateCustomer(customer)
        if not error:
            # customer.password = make_password(customer.password)

            customer.save()
            successful = "Account created successfully"
            return render(request, 'sinup.html', {'success': successful})
            return redirect(request, "homepage")
        else:
            data = {
                'values': values,
                'error': error
            }
        return render(request, 'sinup.html', data)
def validateCustomer(customer):
    error=None
    if (not customer.first_name):
        error = 'First name required!!'
    elif len(customer.first_name) < 4:
        error = 'Enter valid name'
    elif not customer.last_name:
        error = 'Enter last name'
    elif len(customer.last_name) <= 3:
        error = "Enter valid surname"
    elif not str(customer.phone):
        error = 'Enter phone number'
    elif len(str(customer.phone)) != 10:
        error = 'Enter valid phone number'
    elif len(customer.password) < 8:
        error = 'Minimum password length is 8'
    elif str(customer.phone[0]) != str(9):
        error = 'Enter valid phone number '
    elif str(customer.phone[1]) != str(8):
        error = 'Enter valid phone number '
    elif customer.isexistemail():

        error = 'Email already registred'
    elif customer.isexistphone():
        error = 'phone number already registred'
    return error