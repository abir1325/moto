from django.db.models import Count

from django.shortcuts import render
from django.views import View
from .models import Services, Customer
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




