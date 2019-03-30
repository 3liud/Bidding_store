from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	
	def __str__(self):
		return f'{self.user.username} Profile'
	
	def save(self, **kwargs):
		super().save()
		
		img = Image.open(self.image.path)
		
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Profile_Info(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	account = models.CharField(max_length=20, null=False)
	address = models.CharField(max_length=19, null=False, default='0')
	postal_code = models.CharField(max_length=19, null=False, default='0')
	county = models.CharField(max_length=19, null=False, default='0')
	country = models.CharField(max_length=19, null=False, default='0')
