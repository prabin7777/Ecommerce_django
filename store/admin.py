from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.message import Message
from .models.customer import Customer
from .models.orders import Orders

class AdminProduct(admin.ModelAdmin):
    list_display = ["name", "price", "category"]


class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]

class AdminMessage(admin.ModelAdmin):
    list_display = ["msg_date", "recycle_message", "admin_message"]

class Admincustomer(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "email", "password"]

#Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Message, AdminMessage)
admin.site.register(Customer, Admincustomer)
admin.site.register(Orders)
