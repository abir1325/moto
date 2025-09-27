from django.db import models
from django.contrib.auth.models import User



# Create your models here.
STATE_CHOICES=(
        ('Dhaka','Dhaka'),
        ('Chittagong','Chittagong'),
        ('Rajshahi','Rajshahi'),
        ('Jessore','Jessore'),
        ('Rangamati','Rangamati'),
        ('Khagrachari','Khagrachari'),

)
CATEGORY_CHOICES = (
        ('TF','Throttle Fix'),
        ('CM','Carborator Modify'),
        ('CC','Clutch-Change'),
        ('TC','Tire Change'),
        ('TS','Toweing Service'),
        ('FE','Fuel Emergency'),

)
class Services(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default="")
    servapp=models.TextField(default="")
    catagory=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    service_image=models.ImageField(upload_to="services")

    def __str__(self):
        return self.title

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return self.name