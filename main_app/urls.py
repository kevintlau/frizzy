from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path("about/", views.about, name="about"),
	path("search/", views.SearchResultsView.as_view(), name="search_shops"),
	path("shops/", views.ShopList.as_view(), name="shop_index"),
	path("shops/<int:shop_id>/", views.shop_details, name="shop_detail"),

	path("profile/", views.profile, name="profile_detail"),
	path('profile/<int:profile_id>/add_creditcard/', views.add_creditcard, name='add_creditcard'),
	# TODO: add profile update using class-based view
	path("profile/<int:pk>/update/", views.ProfileUpdate.as_view(), name="profile_update"),

	path("creditcards/<int:pk>/update/", views.CreditCardUpdate.as_view(), name="creditcard_update"),
	path("creditcards/<int:pk>/delete/", views.CreditCardDelete.as_view(), name="creditcard_delete"),
	
	# TODO: add order index using class-based view
	path("orders/", views.OrderList.as_view(), name="order_index"),
	path("orders/create/<int:shop_id>", views.OrderCreate.as_view(), name="order_start"),
	# TODO: add order editing and deletion
	path("orders/<int:pk>/update/", views.OrderUpdate.as_view(), name="order_update"),
	path("orders/<int:pk>/delete/", views.OrderDelete.as_view(), name="order_delete"),
	path("orders/<int:pk>/", views.OrderDetail.as_view(), name="order_detail"),

	path("accounts/signup/", views.signup, name="signup"),
]