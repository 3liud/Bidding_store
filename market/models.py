from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PostSell(models.Model):
	title = models.CharField("Input the name of the Item you are selling", max_length=100)
	description = models.TextField("Input some description of the item", null=False, default='')
	commodity = models.ImageField("Let the buyer see what you are selling, upload a picture",
	                              null=False, default='', upload_to='commodity_pics')
	date_posted = models.DateTimeField(default=timezone.now)
	category = models.CharField("Choose product category", max_length=100, default='general')
	price = models.DecimalField("What is the least price you are selling your item for?", max_digits=10,
	                            decimal_places=2, default='')
	sell_on = models.DateTimeField("When do you want your item to go live for Auction?",
	                               default=timezone.now
	                               )
	BID_TIME = (
		('5 minutes', '5'),
		('10 minutes', '10'),
		('20 minutes', '20'),
		('30 minutes', '30'),
	)
	live_time = models.CharField("How long should your item stay in the auction table?", max_length=20, default='5',
	                             choices=BID_TIME
	                             )
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('postsell-detail', kwargs={'pk': self.pk})


class Seller(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	product_id = models.ForeignKey(PostSell, on_delete=models.CASCADE)
	
	def _unicode_(self):
		return str(self.user_name)


class Bidder(models.Model):
	numeric = RegexValidator(r'^[0-9]*$', 'Only numeric are allowed.')
	
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	product_id = models.ForeignKey(PostSell, on_delete=models.CASCADE)
	bid_amount = models.CharField(max_length=255, validators=[numeric])
	
	def _unicode_(self):
		return str(self.user_name)


'''class Bid(models.Model):
	bidder = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return f'{self.item.title} Bidding'
	
	item = models.ForeignKey(PostSell, on_delete=models.CASCADE)
	
	def get_absolute_url(self):
		return reverse('postsell-bid', kwargs={'pk': self.pk})
	
	bid_price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
	bid_time = models.TimeField(default=timezone.now)
	
	def save(self, **kwargs):
		super().save()'''
