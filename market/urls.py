from django.urls import path
import market.views
from . import classviews

urlpatterns = [
	path('', classviews.ProductListView.as_view(), name='market-home'),
	path('user/<username>/', classviews.UserProductListView.as_view(), name='user-post'),
	path('post/<int:pk>/', classviews.ProductDetailView.as_view(), name='product-detail'),
	path('post/new/', classviews.ProductCreateView.as_view(), name='product-create'),
	path('post/viewproducts/', classviews.ProductListView.as_view(), name='view_product'),
	path('bidderlist/<int:pk>/', classviews.BidderListView.as_view(), name="bidder_list"),
	path('post/savebid/', market.views.save_bid, name="save_bid"),
	path('post/<int:pk>/delete/', classviews.ProductDeleteView.as_view(), name='postsell-delete'),
	path('post/<title>/update/', classviews.ProductUpdateView.as_view(), name='postsell-update'),

]
