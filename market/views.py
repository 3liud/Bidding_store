from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from market.models import Product, Bidder
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def get_bid_info_context(pk):
	bidders = Bidder.objects.filter(product_id=pk).order_by('-created')[:6]
	product = Product.objects.get(id=pk)
	context = {'bidders': bidders, 'product': product}
	return context


def bid_information_view(request, pk):
	context = get_bid_info_context(pk)
	return render(request, 'market/product_detail.html', context)


def bid_create(request):
	if request.method == 'POST':
		p_id = request.POST.get('product_id')
		user_id = request.user
		b_amount = int(request.POST.get('bid_amount'))
		if int(b_amount) >= int(request.POST.get('minimum_price')):
			bids = Bidder.objects.filter(product_id=p_id, user_name=user_id)
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
				context = get_bid_info_context(p_id)
				messages.error(request, "bid price should be more than Highest bid amount")
				return render(request, 'market/product_detail.html', context)
			product = Product.objects.filter(id=p_id).first()
			bidder = Bidder.objects.create(user_name=request.user, product_id=product, bid_amount=b_amount)
			bidder.save()
			context = get_bid_info_context(p_id)
			return render(request, 'market/product_detail.html', context)
		context = get_bid_info_context(p_id)
		messages.error(request, "bid price should be more than Highest Bid amount")
		return render(request, 'market/product_detail.html', context)


def get_bidding_time(request):
	product_id = request.GET['product_id']
	data = Product.objects.get(id=product_id)
	sell_on = data.sell_on
	bid_time = data.live_time
	time_data = {
		'sell_on': sell_on,
		'bid_time': bid_time
	}
	return JsonResponse(time_data)


def reset_bid_time(request):
	product_id = request.GET['product_id']
	Product.objects.filter(id=product_id).update(live_time=0)
	return JsonResponse({'msg': 'done'})


def winner_notification(request):
	buffer = io.BytesIO()
	p = canvas.Canvas(buffer)
	p.drawString(100, 100, "Hello There")
	p.showPage()
	p.save()
	return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

# def create_bid(request):
# 	if request.method == 'POST':
# 		p_id = request.POST.get('product_id')
# 		b_amount = int(request.POST.get('bid_amount'))
# 		context = get_bid_info_context(p_id)
# 		if int(b_amount) >= int(request.POST.get('minimum_price')):
# 			bids = Bidder.objects.filter(product_id=p_id)
#
# 			messages.error(request, "bid price should be more than minimum price or the Highest bid price")
#
# 		return render(request, 'market/product_detail.html', context)
# 	else:
# 		x = Bidder.objects.filter(product_id=Product.objects.get
# 		(id=request.POST.get('product_id'))).values('user_name').first()
# 		a = 0
# 		for item in x:
# 			if item['user_name'] == request.user.id:
# 				y = Bidder.objects.get(user_name=request.user.id, product_id=Product.objects.get
# 				(id=request.POST.get('product_id')))
# 				y.bid_amount = int(request.POST.get('bid_amount'))
# 				y.save()
# 				a = 1
# 		if not a:
#
# 			obj = Bidder(user_name=request.user,
# 			             product_id=Product.objects.get(id=request.POST.get('product_id')),
# 			             bid_amount=int(request.POST.get('bid_amount')))
# 			obj.save()
# 		return render(request, 'market/product_detail.html', context)
#
#
# return render(request, 'market/product_detail.html', context)
