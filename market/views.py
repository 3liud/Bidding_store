from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from market.models import Product, Seller, Bidder


def save_bid(request):
	context = dict()
	context['product_list'] = Product.objects.get(id=request.POST.get('product_id'))
	context['seller'] = Seller.objects.get(product_id_id=request.POST.get('product_id'))
	if request.method == 'POST':
		if int(request.POST.get('minimum_price')) > int(request.POST.get('bid_amount')):
			context['error'] = "bid price should be more than minimum price"
			return render(request, 'market/product_detail.html', context)
		else:
			x = Bidder.objects.filter(product_id=Product.objects.get(id=request.POST.get('product_id'))).values(
				'user_name')
			a = 0
			for item in x:
				if item['user_name'] == request.user.id:
					y = Bidder.objects.get(user_name=request.user.id, product_id=Product.objects.get(
						id=request.POST.get('product_id')))
					y.bid_amount = int(request.POST.get('bid_amount'))
					y.save()
					a = 1
			if not a:
				obj = Bidder(user_name=request.user, product_id=Product.objects.get(id=request.POST.get('product_id')),
				             bid_amount=int(request.POST.get('bid_amount')))
				obj.save()
			return HttpResponseRedirect(reverse('view-product'))
	return render(request, 'market/product_detail.html', context)
