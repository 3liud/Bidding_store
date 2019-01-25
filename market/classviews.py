from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Product, Seller, Bidder
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
		'posts': Product.objects.all()
	}
	return render(request, 'market/home.html', context)


class ProductListView(ListView):
	model = Product
	template_name = 'market/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5


class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	fields = ['title', 'image', 'description', 'category', 'price', 'sell_on', 'live_time']
	
	def form_valid(self, form):
		obj = Seller(user_name=self.request.user, product_id=form.save())
		obj.save()
		return super().form_valid(form)
	
	def get_success_url(self):
		return reverse('market-home')


class ProductDetailView(DetailView):
	model = Product


class UserProductListView(ListView):
	model = Product
	template_name = 'market/user_product.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'user-post'
	paginate_by = 5
	
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Product.objects.filter(author=user).order_by('-date_posted')


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Product
	fields = ['title', 'content']
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Product
	success_url = '/'
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class BidderListView(ListView):
	model = Bidder
	
	def get_queryset(self):
		return Bidder.objects.filter(product_id=self.kwargs['pk'])
	
	def get_context_data(self, **kwargs):
		context = super(BidderListView, self).get_context_data(**kwargs)
		context["product_id"] = self.kwargs['pk']
		return context


def about(request):
	return render(request, 'market/about.html', {'title': 'About'})
