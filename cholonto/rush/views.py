from django.db.models import Count
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.views import View
from .models import Services, Customer, Product, Cart
from .forms import RegistrationForm, CustomerProfileForm
from django.contrib import messages

def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class CatagoryView(View):
    def get(self,request,val):
        services=Services.objects.filter(catagory=val)
        title=Services.objects.filter(catagory=val).values('title')
        return render(request,"app/catagory.html",locals())

class CatagoryTitle(View):
    def get(self,request,val):
        services=Services.objects.filter(title=val)
        title=Services.objects.filter(catagory=services[0].catagory).values('title')
        return render(request,"app/catagory.html",locals())




class ServicesDetail(View):
    def get(self,request,pk):
        services = Services.objects.get(pk=pk)
        return render(request,"app/services_detail.html",locals())



class RegistrationView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,"app/registration.html",locals())

    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successful")

        else:
            messages.warning(request,"Registration failed")

        return render(request, "app/registration.html", locals())

class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,"app/profile.html",locals())
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']

            reg=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Profile saved successfully")

        else:
            messages.warning(request,"Profile not saved")

        return render(request,"app/profile.html",locals())


def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,"app/address.html",locals())


class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,"app/updateAddress.html",locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add= Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Address updated successfully")
        else:
            messages.warning(request,"Address not updated")
            return redirect("address")
        return render(request,"app/updateAddress.html",locals())

def add_to_cart(request):
    user=request.user
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")

def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount += value
    return render(request,"app/addtocart.html",locals())

class checkout(View):
    def get(self,request):
        return render(request,"app/checkout.html",locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(user=request.user, product=Product.objects.get(id=prod_id))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        print(prod_id)
        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + c.quantity * c.product.discounted_price,

        }
        return JsonResponse({'success': True})


def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(user=request.user, product=Product.objects.get(id=prod_id))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        print(prod_id)
        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + c.quantity * c.product.discounted_price,

        }
        return JsonResponse({'success': True})



def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(user=request.user, product=Product.objects.get(id=prod_id))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        print(prod_id)
        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + c.quantity * c.product.discounted_price,

        }
        return JsonResponse({'success': True})
