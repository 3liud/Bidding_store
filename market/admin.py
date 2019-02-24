from django.contrib import admin
from .models import Product, Bidder, Bid

admin.site.register(Product)
admin.site.register(Bid)
admin.site.register(Bidder)
