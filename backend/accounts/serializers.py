from django import forms

class user_login_serializer(forms.Form):
    email       = forms.EmailField(max_length=60)
    password    = forms.CharField(widget=forms.PasswordInput())
    