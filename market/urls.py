from django.urls import path
import market.views
from . import classviews

urlpatterns = [
	path('home/', classviews.ProductListView.as_view(), name='market-home'),
	path('post/agriculture/', classviews.AgriProdListView.as_view(), name='agri-product'),
	path('product-detail/<int:pk>/', market.views.bid_information_view, name='product-detail'),
	path('post/new/', classviews.ProductCreateView.as_view(), name='product-create'),
	path('post/viewproduct/', classviews.ProductListView.as_view(), name='view-product'),
	path('post/bidderlist/<int:pk>/', classviews.BidderListView.as_view(), name="bidder-list"),
	path('post/createbid/', market.views.bid_create, name="create-bid"),
	path('post/<int:pk>/delete/', classviews.ProductDeleteView.as_view(), name='product-delete'),
	path('post/<int:pk>/update/', classviews.ProductUpdateView.as_view(), name='product-update'),
	path('user/<user_name>/', classviews.UserProductListView.as_view(), name='user-posts'),
	path('', market.classviews.about, name='about'),
	path('get_bidding_time/', market.views.get_bidding_time, name='get_bidding_time'),
	path('pay/<int:pk>', market.views.make_pay, name='pay'),
	path('reset_bid_time/', market.views.reset_bid_time, name='reset_bid_time')
]
