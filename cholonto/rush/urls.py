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

from .forms import LoginForm, PasswordResetForm, RegistrationForm, MyPasswordChangeForm,MySetPasswordForm
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.home ),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('catagory/<slug:val>',views.CatagoryView.as_view() , name='catagory'),
    path('catagory-title/<val>', views.CatagoryTitle.as_view() , name='catagory-title'),
    path('services-detail/<int:pk>',views.ServicesDetail.as_view() , name='services-detail'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/', views.address, name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.show_cart, name='checkout'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),


                  #login authentication
    path('registration/',views.RegistrationView.as_view() , name='registration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm ), name='login'),
    path('passwrodchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/ passwordchangedone'), name='passwordchange'),
    path('passwordchnagedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=PasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html,form_class=MySetPasswordForm'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
