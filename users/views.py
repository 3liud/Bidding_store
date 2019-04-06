from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, UserAddressForm, ProfileUpdateForm, UserAccountForm
from django.contrib.auth.decorators import login_required
from market.models import Bidder


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created, you are now able to log in!')
			return redirect('profile')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated successfully')
			return redirect('profile')
	
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)


@login_required
def account(request):
	if request.method == 'POST':
		a_form = UserUpdateForm(request.POST, instance=request.user)
		if a_form.is_valid():
			a_form.save()
			messages.success(request, f'Your account has been updated successfully')
			return redirect('profile')
	
	else:
		a_form = UserAccountForm(instance=request.user)
	
	context = {
		'a_form': a_form,
	}
	return render(request, 'users/payment_details.html', context)


@login_required
def address(request):
	if request.method == 'POST':
		ad_form = UserUpdateForm(request.POST, instance=request.user)
		if ad_form.is_valid():
			ad_form.save()
			messages.success(request, f'Your account has been updated successfully')
			return redirect('profile')
	
	else:
		ad_form = UserAddressForm(instance=request.user)
	
	context = {
		'ad_form': ad_form,
	}
	return render(request, 'users/address.html', context)


def reset_bid_time(request):
    product_id = request.GET['product_id']
    Bidder.objects.filter(id=product_id).update(live_time=0)
    
