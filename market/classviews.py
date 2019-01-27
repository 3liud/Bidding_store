from django.shortcuts import render
from django.urls import reverse
from .models import Product, Seller, Bidder
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
	context_object_name = 'product-list'
	
	def get_context_data(self, **kwargs):
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		x = Seller.objects.all()
		context['Seller'] = Seller.objects.get(product_id_id=self.kwargs['pk'])
		return context


def get_success_url():
	return reverse('market-home')


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Seller
	fields = ['title', 'description']
	
	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	def test_func(self):
		pass
	
	model = Product
	success_url = '/'
	
	def get_context_data(self, **kwargs):
		context = super(ProductDeleteView, self).get_context_data(**kwargs)
		context["product_id"] = self.kwargs['pk']
		return context
	
	def get_success_url(self):
		return reverse('view-product')
	

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


'''
class UserProductListView(ListView):
	model = Seller
	template_name = 'market/user_product.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'user-post'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, seller=self.kwargs.get('username'))
		return Product.objects.filter(seller=user).order_by('-date_posted')
'''