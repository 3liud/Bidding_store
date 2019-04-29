from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)

from .models import *
from .models import Product, Bidder


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    context_object_name = 'posts'
    queryset = Product.objects.filter(category__icontains='relic')
    ordering = ['-date_posted']
    paginate_by = 6
    template_name = 'market/home.html'


class AgriProdListView(ListView):
    model = Product

    context_object_name = 'posts'
    queryset = Product.objects.filter(category__icontains='agriculture')
    ordering = ['-date_posted']
    paginate_by = 6
    template_name = 'market/home.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'image', 'description', 'category', 'type', 'price', 'sell_on', 'live_time']

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
    fields = ['image', 'description', 'price', 'sell_on', 'live_time', 'category', 'type']

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


class FProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False


class BidderListView(ListView):
    model = Bidder
    template_name = 'market/bidder_list.html'

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


class UserProductWonListView(ListView):
    model = Bidder
    template_name = 'users/Itemswon.html'

    def get_queryset(self):
        items = Bidder.objects.filter(bid_status='WINNER')
        print(items)
        return items
