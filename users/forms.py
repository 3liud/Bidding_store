from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Account, Address


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['image']


class UserAccountForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['cardNumber', 'Account_Balance', 'email']


class UserAddressForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Address
        fields = ['county', 'country', 'address', 'email', 'postal_code']
