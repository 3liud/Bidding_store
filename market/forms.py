from django import forms

from market.models import Bid


class BidForm(forms.ModelForm):

	class Meta:
		model = Bid
		fields = ['bid_price']
