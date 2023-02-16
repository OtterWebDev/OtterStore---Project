from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from .forms import CustomerForm, UserForm, VendorForm
from .models import User, UserCustomer, UserVendor
from .multiforms import MultiFormsView


def form_redir(request):
    return render(request, 'pages/accounts/login.html')

def multiple_forms(request):
    if request.method == 'POST':
        user_form       = UserForm(request.POST)
        vendor_form     = VendorForm(request.POST,request.FILES)    
        if user.is_valid():
            first_name              = user_form['first_name']
            last_name               = user_form['last_name'] 
            birth_date              = user_form['birt_date']
            phone_number            = user_form['phone_number']
            country                 = user_form['country']
            state                   = user_form['state']
            city                    = user_form['city']
            address_line            = user_form['address_line']
            username                = user_form['username']
            email                   = user_form['email']
            password                = user_form['password']               
            user                    = User.objects.create_user(first_name=first_name,last_name=last_name,birth_date=birth_date,phone_number=phone_number,country=country,state=state,city=city,address_line=address_line,username=username,email=email,password=password)
            user.role               = User.CUSTOMER                             
            user.save()
            return HttpResponseRedirect(reverse('home'))     
           
        elif vendor_form.is_valid() and user_form.is_valid():
            first_name              = user_form.cleaned_data['first_name']
            last_name               = user_form.cleaned_data['last_name'] 
            phone_number            = user_form.cleaned_data['phone_number']
            username                = user_form.cleaned_data['username']
            email                   = user_form.cleaned_data['email']
            password                = user_form.cleaned_data['password']
            birth_date              = user_form.cleaned_data['birth_date']
            country                 = user_form.cleaned_data['country']
            state                   = user_form.cleaned_data['state']
            city                    = user_form.cleaned_data['city']
            address_line            = user_form.cleaned_data['address_line']               
            user                    = User.objects.create_user(first_name=first_name,last_name=last_name,birth_date=birth_date,phone_number=phone_number,username=username,email=email,password=password,address_line=address_line,country=country,city=city,state=state)
            user.role               = User.VENDOR                             
            user.save() 
            vendor                  = vendor_form.save(commit=False)
            vendor.user             = user
            vendor.save()    
            return HttpResponseRedirect(reverse('home'))  
                              
    else:
        user_form = UserForm()
        customer_form = CustomerForm()
        vendor_form = VendorForm()
            
    return render(request, 'pages/accounts/login.html', {
        'user_form': user_form,
        'customer_form': customer_form,
        'vendor_form': vendor_form,
    })

class Accounts(MultiFormsView):
    template_name = 'pages/accounts/login.html'
    form_classes = {'user': UserForm, 'vendor': VendorForm, 'customer':CustomerForm}
    success_urls = {'vendor': reverse_lazy('home'), 'customer': reverse_lazy('home'),'user': reverse_lazy('home') }
    
    
    def user_form_valid(self,form):          
        form_name = form.cleaned_data.get('action')

        return HttpResponseRedirect(self.get_success_url(form_name))
    
    def vendor_form_valid(self,form):          
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

    

    

        
        
    """ def login(request):
        if request.method == 'POST':
            email           = request.POST['email']
            password        = request.POST['password']
            user            = auth.authenticate(email=email,password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request,'You are now logged in')
                return redirect('home')
            else:
                messages.error(request,'Invalid login credentials')
                return redirect('login') """

