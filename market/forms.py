from django import forms
from market.models import Product


class BidForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['price']
