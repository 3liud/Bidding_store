from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import PostSell, Bid
from django.contrib.auth.decorators import login_required
from .forms import PlaceBid
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	DeleteView,
	UpdateView
)


def home(request):
	context = {
		'posts': PostSell.objects.all(),
		'postedbids': Bids.objects.all()
	}
	return render(request, 'market/home.html', context)


class PostSellListView(ListView):
	model = PostSell
	template_name = 'market/home.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 3


class UserPostSellListView(ListView):
	model = PostSell
	template_name = 'market/user_post.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 3
	
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return PostSell.objects.filter(seller=user).order_by('-date_posted')


class PostSellDetailView(DetailView):
	model = PostSell


class PostSellBidDetail(DetailView):
	model = Bid


class PostSellBidDetailView(DetailView):
	model = Bid

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.seller:
			return False
		return False


class PostSellCreateView(LoginRequiredMixin, CreateView):
	model = PostSell
	fields = ['title', 'description', 'commodity', 'price']
	
	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)
	

class PostSellUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = PostSell
	fields = ['title', 'description', 'commodity', 'price']
	
	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.seller:
			return True
		return False


class PostSellDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = PostSell
	success_url = '/'
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.seller:
			return True
		return False


def about(request):
	return render(request, 'market/about.html', {'title': 'About'})


@login_required
def bid(request):
	if request.method == 'POST':
		bid_form = PlaceBid(request.POST, instance=request.user)
		if bid_form.is_valid():
			bid_form.save()
			messages.success(request, f'Your account has been updated successfully')
			return redirect('market-home')
	
	else:
		bid_form = PlaceBid(instance=request.user)
	
	context = {
		'bid_form': bid_form,
	}
	return render(request, 'market/postsell_detail.html', context)

