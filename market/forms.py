from django import forms
from .models import Bid


class PlaceBid(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model = Bid
		fields = ['bid_price']