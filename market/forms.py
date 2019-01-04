from django import forms
from .models import PostSell


'''class UserRegisterForm(UserCreationForm):
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
	class Meta:
		model = Profile
		fields = ['image']'''


class SellItemForm(forms.ModelForm):
	class Meta:
		model = PostSell
		fields = ['description', 'title', 'commodity', 'price']
