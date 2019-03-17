from django.urls import path
import market.views
from . import classviews

urlpatterns = [
	path('', classviews.ProductListView.as_view(), name='market-home'),
	path('home/', classviews.ProductListView.as_view(), name='market-home'),
	path('product-detail/<int:pk>/', market.views.bid_information_view, name='product-detail'),
	path('post/new/', classviews.ProductCreateView.as_view(), name='product-create'),
	path('post/viewproduct/', classviews.ProductListView.as_view(), name='view-product'),
	# path('post/bidderlist/<int:pk>/', classviews.BidderListView.as_view(), name="bidder-list"),
	path('post/createbid/', market.views.bid_create, name="create-bid"),
	# path('post/createbid/', market.views.create_bid, name="create-bid"),
	path('post/<int:pk>/delete/', classviews.ProductDeleteView.as_view(), name='product-delete'),
	path('post/<int:pk>/update/', classviews.ProductUpdateView.as_view(), name='product-update'),
	path('user/<user_name>/', classviews.UserProductListView.as_view(), name='user-posts'),
	path('about/', market.classviews.about, name='about'),
]
