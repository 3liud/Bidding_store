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
	price = models.DecimalField("How much are you selling the item for?", max_digits=10,
	                            decimal_places=2, default='')
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('postsell-detail', kwargs={'pk': self.pk})
#	bid_list = models.TextField("existing bids")
	

class Bid(models.Model):
	bidder = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.bidder)
	
	item = models.ForeignKey(PostSell, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('postsell-bid', kwargs={'pk': self.pk})

	bid_price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
	BID_TIME = (
		('5 minutes', '5'),
		('10 minutes', '10'),
		('20 minutes', '20'),
		('30 minutes', '30'),
			)
	bid_time = models.CharField(max_length=20, default='5', choices=BID_TIME)
