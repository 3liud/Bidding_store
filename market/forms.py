from django import forms
from market.models import Product
from django.utils import timezone


class BidForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['price']
