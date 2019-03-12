from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import datetime
from django.shortcuts import render
from django.urls import reverse
from market.models import Product, Bidder
from django.db.models import  Max


def get_bid_info_context(pk):
	bidders = Bidder.objects.filter(product_id=pk).order_by('-created')[:6]
	product = Product.objects.get(id=pk)
	context = {'bidders': bidders, 'product': product}
	return  context


def bid_informaion_view(request, pk):
	context = get_bid_info_context(pk)
	return render(request, 'market/product_detail.html', context)


def bid_create(request):
	# time = datetime.datetime.now()
	# sell_date = Product.sell_on
	# global context
	if request.method == 'POST':
		# context = dict()
		# p_id = int(request.POST.get('product_id'))
		# context['product_list'] = Product.objects.get(id=p_id)
		# context['buyer'] = request.user
		# bidder = request.user
		p_id = request.POST.get('product_id')
		b_amount = int(request.POST.get('bid_amount'))
		if int(b_amount) >= int(request.POST.get('minimum_price')):
			bids = Bidder.objects.filter(product_id=p_id)
			if bids:
				min_price = 0
				for bid in bids:
					if int(bid.bid_amount) > min_price:
						min_price = int(bid.bid_amount)
				if int(b_amount) >= int(min_price):
					bid = Bidder.objects.filter(user_name=request.user)
					if not bid:
						product = Product.objects.filter(id=p_id).first()
						bidder = Bidder.objects.create(user_name=request.user, product_id=product, bid_amount=b_amount)
						bidder.save()
						context = get_bid_info_context(p_id)
						return render(request, 'market/product_detail.html', context)
					bid.update(bid_amount=b_amount)
					context = get_bid_info_context(p_id)
					return render(request, 'market/product_detail.html', context)
					# context = get_bid_info_context(p_id)
					# context['error'] = "Max no of bids reached"
					# messages.error(request, "Max no if bids reached")
					# return render(request, 'market/product_detail.html', context)
				context = get_bid_info_context(p_id)
				context['error'] = "The bid price should be more than the minimum bid amount"
				messages.error(request, "bid price should be more than minimum bid amount")
				return render(request, 'market/product_detail.html', context)
			product = Product.objects.filter(id=p_id).first()
			bidder = Bidder.objects.create(user_name=request.user, product_id=product, bid_amount=b_amount)
			bidder.save()
			context = get_bid_info_context(p_id)
			return render(request, 'market/product_detail.html', context)
			
		context = get_bid_info_context(p_id)
		context['error'] = "The bid price should be more than the minimum price"
		messages.error(request, "bid price should be more than minimum price")
		return render(request, 'market/product_detail.html', context)
	# if request.method == 'POST':
		# 	if int(request.POST.get('minimum_price')) > int(request.POST.get('bid_amount')):
		# 		context['error'] = "The bid price should be more than the minimum price"
		# 		# messages.error(request, "bid price should be more than minimum price")
		#
		# 		return render(request, 'market/bidder_list.html', context)
		# 	else:
		# 		x = Bidder.objects.filter(product_id=Product.objects.get
		# 		(id=request.POST.get('product_id'))).values('user_name')
		# 		a = 0
		# 		for item in x:
		# 			if item['user_name'] == request.user.id:
		# 				y = Bidder.objects.get(user_name=request.user.id, product_id=Product.objects.get
		# 					(id=request.POST.get('product_id')))
		# 				y.bid_amount = int(request.POST.get('bid_amount'))
		# 				y.save()
		# 				a = 1
		# 		if not a:
		# 			obj = Bidder(user_name=request.user,
		# 			             product_id=Product.objects.get(id=request.POST.get('product_id')),
		# 			             bid_amount=int(request.POST.get('bid_amount')))
		# 			obj.save()
		# 		return HttpResponseRedirect(reverse('view-product'))

	return render(request, 'market/product_detail.html', context)
