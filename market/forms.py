from django import forms
from .models import PostSell


class PostSellUpdateForm(forms.ModelForm):
	class Meta:
		model = PostSell
		fields = ['image']
