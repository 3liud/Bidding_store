from django.urls import path
import market.views
from . import classviews

urlpatterns = [
	path('', market.views.index, name='index'),
	path('home/', classviews.ProductListView.as_view(), name='market-home'),
	path('post/<int:pk>/', classviews.ProductDetailView.as_view(), name='product-detail'),
	path('post/new/', classviews.ProductCreateView.as_view(), name='product-create'),
	path('post/viewproduct/', classviews.ProductListView.as_view(), name='view-product'),
	path('post/bidderlist/<int:pk>/', classviews.BidderListView.as_view(), name="bidder_list"),
	path('post/createbid/', market.views.bid_create, name="create-bid"),
	path('post/<int:pk>/delete/', classviews.ProductDeleteView.as_view(), name='product-delete'),
	path('post/<int:pk>/update/', classviews.ProductUpdateView.as_view(), name='product-update'),
	path('user/<user_name>/', classviews.UserProductListView.as_view(), name='user_posts'),
	path('trial/', classviews.ProductListView2.as_view(), name='market-trialhome'),
]
