
from django import forms

from .models import User, UserCustomer, UserVendor


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class UserForm(forms.ModelForm,MultipleForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model =  User
        fields = ['first_name','last_name','birth_date','phone_number','email','username','password','country','state','city','address_line','role']
        
    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match")
    
class VendorForm(forms.ModelForm,MultipleForm):
   
    class Meta():
        model = UserVendor
        fields =['vendor_name','vendor_description','vendor_license']
    
class CustomerForm(MultipleForm):
    
    class Meta():
        model = UserCustomer
        fields = ['profile_picture','cover_photo']

class LoginForm(MultipleForm,forms.Form):
     pass

    


    
 
