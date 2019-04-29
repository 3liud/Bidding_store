from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# from django.db.backends.sqlite3.base import DatabaseWrapper
# DatabaseWrapper.data_types = DatabaseWrapper._data_types


class Product(models.Model):
    title = models.CharField("Input the title of the Item you are selling", max_length=30)
    description = models.TextField("Input some description of the item", null=False, default='')
    image = models.ImageField("Let the buyer see what you are selling, upload a picture",
                              null=False, default='', upload_to='commodity_pics')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    CATEGORY = (
        ('Relic', 'Relic'),
        ('Agriculture', 'Agriculture')
    )
    TYPE = (
        ('Painting', 'Painting'),
        ('Sculpture', 'Sculpture'),
        ('Book', 'Book'),
        ('Instrument', 'Instrument'),
        ('Milk', 'Milk'),
        ('Tea', 'Tea'),
        ('Maize', 'Maize')
    )
    category = models.CharField("Choose product category", max_length=100, default='Gen', choices=CATEGORY)
    type = models.CharField("Choose product type", max_length=100, default='Painting', choices=TYPE)
    price = models.IntegerField("What is the least/(unit) price you are selling your item for?")
    sell_on = models.DateTimeField(default=timezone.now)
    BID_TIME = (
        ('5', '5 minutes'),
        ('10', '10 minutes'),
        ('30', '30 minutes'),
        ('60', '1 Hour'),
        ('720', '1 month'),
        ('1440', '2 months'),
        ('2160', '3 Months')
    )
    live_time = models.CharField("How long should your item stay in the auction table?", max_length=20, default='5',
                                 choices=BID_TIME
                                 )
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default='2')

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class Bidder(models.Model):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric are allowed.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_amount = models.CharField(max_length=255, validators=[numeric])
    Status = (
        ('PENDING', '0'),
        ('WINNER', '1'))

    bid_status = models.CharField(max_length=20, choices=Status, default='PENDING')

    def _unicode_(self):
        return str(self.user_name)


