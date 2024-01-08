from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from .models import Items, Orders, UserProfile
from django.contrib.auth.hashers import make_password

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = UserProfile
        fields = ['fullname', 'emailid']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')  
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class SigninForm(forms.Form):
    emailid = forms.EmailField(label='Emailid')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['itemname', 'image', 'price', 'category', 'description']
        
class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_id','itemname', 'image', 'price', 'category', 'description']
        
class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['itemname', 'price', 'quantity', 'totalamount']
        
# class UpdateOrderForm(forms.ModelForm):
#     class Meta:
#         model = Orders
#         fields = ['itemname', 'price', 'quantity', 'totalamount']