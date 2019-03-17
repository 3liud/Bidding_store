from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Product, Bidder
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	DeleteView,
	UpdateView
)


class ProductListView(LoginRequiredMixin, ListView):
	model = Product
	template_name = 'market/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 6
	

# class ProductListView2(LoginRequiredMixin, ListView):
# 	model = Product
# 	template_name = 'market/trialhome.html'
# 	context_object_name = 'posts'
# 	ordering = ['-date_posted']
# 	paginate_by = 6


class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	fields = ['title', 'image', 'description', 'category', 'price', 'sell_on', 'live_time']
	
	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)
	
	def get_success_url(self):
		return reverse('market-home')


class ProductDetailView(DetailView):
	model = Product
	context_object_name = 'product_list'
	
	def get_context_data(self, **kwargs):
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		x = Product.objects.all()
		bidders = Bidder.objects.filter(product_id=self.kwargs['pk']).order_by('-created')[:6]
		seller = Product.objects.get(id=self.kwargs['pk'])
		context = {'bidders': bidders, 'product': seller}
		print(context)
		return context

	
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Product
	fields = ['image', 'description', 'price', 'sell_on', 'live_time']
	
	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.seller:
			return True
		return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Product
	success_url = '/'
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.seller:
			return True
		return False


class BidderListView(ListView):
	model = Bidder
	
	def get_queryset(self):
		return Bidder.objects.filter(product_id=self.kwargs['pk']).order_by('-created')[:6]
		
	def get_context_data(self, **kwargs):
		context = super(BidderListView, self).get_context_data(**kwargs)
		context["product_id"] = self.kwargs['pk']
		return context


def about(request):
	return render(request, 'market/about.html', {'title': 'About'})


class UserProductListView(ListView):
	model = Product
	template_name = 'market/user_product.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'user_posts'
	paginate_by = 5
	
	def get_queryset(self):
		user = get_object_or_404(User, seller=self.kwargs.get('username'))
		return Product.objects.filter(seller=user).order_by('-date_posted')
