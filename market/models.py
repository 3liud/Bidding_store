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
	#time = models.CharField(max_length=5)
	#live_date = models.DateField(default==)
	price = models.DecimalField("How much are you selling the item for?", max_digits=10,
	                            decimal_places=2, default='')
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('postsell-detail', kwargs={'pk': self.pk})


class Bid(models.Model):
	bid_price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
	bidder = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.bidder
	
	item = models.ForeignKey(PostSell, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.item
	
