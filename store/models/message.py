from django.db import models
class Message(models.Model):
    msg_date=models.IntegerField()
    recycle_message=models.CharField(max_length=2000)
    admin_message = models.CharField(max_length=2000)
    sale_image=models.ImageField(upload_to="uploads/products/")
    @staticmethod
    def get_all_message():
        return Message.objects.all()


    def __str__(self):
        return self.name