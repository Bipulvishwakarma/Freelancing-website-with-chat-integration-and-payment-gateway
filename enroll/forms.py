from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Product
from .models import Order
from .models import OrderItem
from .models import Delivery
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Enter password',
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='confirm password (again)',
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields= "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"


class OrderItemForm(forms.ModelForm):
    class Meta:
        model=OrderItem
        fields=['product','quantity']

class Delivery(forms.ModelForm):
    class Meta:
        model=Delivery
        fields=["name","description"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }    

class Edituserprofile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined']
        labels={'email':'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            
            'date_joined':forms.TextInput(attrs={'class': 'form-control'}),
        }



        '''
        fields=['name','email','country']
        labels={'email':'Email'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            '''