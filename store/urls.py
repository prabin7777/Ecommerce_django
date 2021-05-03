

from django.contrib import admin
from django.urls import path
from .views.sinup import sinup
from .views.login import login ,logout
from .views.home_views import  Index,Recycle
from .views.cart import Cart

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('sinup',sinup.as_view(), name="sinup"),
    path('recycle',Recycle.as_view(), name="recycle"),
    path('login',login.as_view(), name="login"),
    path('logout',logout, name="logout"),
    path('cart',Cart.as_view(), name="cart")
    
]
