from django.contrib import admin
from .models import Services, Customer, Product, Cart


@admin.register(Services)

class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','catagory', 'description','service_image']




@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','description','product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city', 'state','zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']





