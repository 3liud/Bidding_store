from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



from market.models import Product, Bidder


def bid_create(request):

	if request.method == 'POST':
		context = dict()
		context['product_list'] = Product.objects.get(id=request.POST.get('product_id'))
		# user =
		context['buyer'] = request.user
		if int(request.POST.get('minimum_price')) > int(request.POST.get('bid_amount')):
			
			messages.error(request, "bid price should be more than minimum price")
			return render(request, 'market/bidder_list.html', context)
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
	return render(request, 'market/bidder_list.html', context)


def index(request):
	return render(request, 'market/index.html')
