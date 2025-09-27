"""
URL configuration for cholonto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .forms import LoginForm,PasswordResetForm,RegistrationForm
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.home ),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('catagory/<slug:val>',views.CatagoryView.as_view() , name='catagory'),
    path('catagory-title/<val>', views.CatagoryTitle.as_view() , name='catagory-title'),
    path('services-detail/<int:pk>',views.ServicesDetail.as_view() , name='services-detail'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/', views.ProfileView.as_view(), name='address'),

                  #login authentication
    path('registration/',views.RegistrationView.as_view() , name='registration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm ), name='login'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=PasswordResetForm),name='password_reset'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
