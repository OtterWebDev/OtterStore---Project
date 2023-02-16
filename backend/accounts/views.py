from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.http import urlsafe_base64_decode

from .forms import CustomerForm, LoginForm, UserForm, VendorForm
from .models import User, UserCustomer, UserVendor
from .multiforms import MultiFormsView
from .serializers import user_login_serializer


class Accounts(MultiFormsView):
    template_name = 'pages/accounts/login.html'
    form_classes = {'user':UserForm,'vendor':VendorForm,'customer':CustomerForm,'login': LoginForm}
    user_vendor = {'user': UserForm ,'vendor':VendorForm}
    user_customer = {'user': UserForm,'customer':CustomerForm}
    grouped_forms = {'user_vendor': user_vendor, 'user_customer':user_customer}
    success_urls = {'user_customer':reverse_lazy('home'),'user_vendor':reverse_lazy('home'),'login': reverse_lazy('home')}

     
    def user_valid(self,form):
        first_name              = form.cleaned_data.get('first_name')
        last_name               = form.cleaned_data.get('last_name')
        birth_date              = form.cleaned_data.get('birth_date')
        phone_number            = form.cleaned_data.get('phone_number')
        country                 = form.cleaned_data.get('country')
        state                   = form.cleaned_data.get('state')
        city                    = form.cleaned_data.get('city')
        address_line            = form.cleaned_data.get('address_line')
        username                = form.cleaned_data.get('username')
        email                   = form.cleaned_data.get('email')
        password                = form.cleaned_data.get('password')
        user                    = User.objects.create_user(first_name=first_name,last_name=last_name,birth_date=birth_date,phone_number=phone_number,country=country,state=state,city=city,address_line=address_line,username=username,email=email,password=password)
        user.role               = User.CUSTOMER                             
        user.save()
        return HttpResponseRedirect(self.get_success_url('user_customer'))

    def user_vendor_valid(self,form):
        first_name              = form.cleaned_data.get('first_name')
        last_name               = form.cleaned_data.get('last_name')
        birth_date              = form.cleaned_data.get('birth_date')
        phone_number            = form.cleaned_data.get('phone_number')
        country                 = form.cleaned_data.get('country')
        state                   = form.cleaned_data.get('state')
        city                    = form.cleaned_data.get('city')
        address_line            = form.cleaned_data.get('address_line')
        username                = form.cleaned_data.get('username')
        email                   = form.cleaned_data.get('email')
        password                = form.cleaned_data.get('password')
        user                    = User.objects.create_user(first_name=first_name,last_name=last_name,birth_date=birth_date,phone_number=phone_number,country=country,state=state,city=city,address_line=address_line,username=username,email=email,password=password)
        user.role               = User.VENDOR                            
        user.save()
        vendor_form             = VendorForm()
        vendor                  = vendor_form.save(commit=False)
        vendor.user             = user
        vendor.save()
        return HttpResponseRedirect(self.get_success_url('user_vendor'))

    def login_valid(self,request):
        user                    = authenticate(email=request.data['email'],password=request.data['password'])
        if user is not None:
            login(request,user)    
            return HttpResponseRedirect(self.get_success_url('login'))         
        else:
            print('erro')
            return render(request,'accounts/login.html')
                