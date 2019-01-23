from django.urls import path
from . import classviews
from .classviews import (
	PostSellDeleteView,
	PostSellDetailView,
	PostSellListView,
	PostSellUpdateView,
	UserPostSellListView,
	PostSellCreateView,
	BidderListView
	)

urlpatterns = [
	path('', PostSellListView.as_view(), name='market-home'),
	path('user/<int:pk>/', UserPostSellListView.as_view(), name='user-post'),
	path('post/<int:pk>/', PostSellDetailView.as_view(), name='postsell-detail'),
	path('postsell/new/', PostSellCreateView.as_view(), name='postsell-create'),
	path('post/<int:pk>/update/', PostSellUpdateView.as_view(), name='postsell-update'),
	path('post/<int:pk>/delete/', PostSellDeleteView.as_view(), name='postsell-delete'),
	path('post/<int:pk>/bidderlist', BidderListView.as_view(), name='bidder_list'),
	#path('bid/add', PostSellBidDetail.as_view(), name='postsell-bid'),
	#path('post/<int:pk>/', PostSellBidDetailView.as_view(), name='bid-detail'),
	#path('about/', classviews.about, name='market-about'),
]
