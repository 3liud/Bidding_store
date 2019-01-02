from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PostSell(models.Model):
	title = models.CharField(max_length=50)
	commodity = models.ImageField(null=True, upload_to='commodity_pics')
	description = models.TextField(max_length=300, null=True)
	date_posted = models.DateTimeField(default=timezone.now)
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	
	def __str__(self):
		return str(self) + ":$" + str(self.price)
		
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('postsell-detail', kwargs={'pk': self.pk})
