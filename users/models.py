from django.db import models
from django.core.validators import RegexValidator
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


class Account(models.Model):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric are allowed.')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    cardNumber = models.CharField(max_length=30, default='AUCT-010')
    Account_Balance = models.CharField(max_length=20, default=100000, validators=[numeric])


class Address(models.Model):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric are allowed.')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, default='Kenya')
    address = models.CharField(max_length=19, null=False, default='0000')
    postal_code = models.CharField(max_length=19, null=False, default='0000')
    county = models.CharField(max_length=19, null=False, default='Nairobi')
