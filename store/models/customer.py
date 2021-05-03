from django.db import models
class Customer(models.Model):
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    adress=models.CharField(max_length=500)
    password=models.CharField(max_length=500)

    def isexistemail(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False
    def isexistphone(self):
        if Customer.objects.filter(phone = self.phone):
            return True
        else:
            return False
    @staticmethod
    def get_all_component():
        return Customer.objects.all()
    @staticmethod
    def get_customer_by_phone(phone):
       return Customer.objects.filter(phone=phone)
    def get_customer_by_password(password):
       return Customer.objects.filter(password=password)







