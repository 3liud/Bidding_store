from django import forms
from market.models import Product

from market.models import Bid


class BidForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['price']
