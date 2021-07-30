from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path("about/", views.about, name="about"),
	path("search/", views.SearchResultsView.as_view(), name="search_shops"),
	path("shops/<int:shop_id>/", views.shop_details, name="shop_detail"),

	# path("profile/<int:pk>/", views.ProfileDetail.as_view(), name="profile_detail"),
	path("profile/", views.profile, name="profile_detail"),
	path("profile/create/", views.ProfileCreate.as_view(), name="profile_create"),
	path("profile/<int:pk>/update/", views.ProfileUpdate.as_view(), name="profile_update"),

	path("creditcards/", views.CreditCardDetail.as_view(), name="creditcard_index"),
	# TEST: add profile_pk here so the form can know which user to link the new card to
	path("creditcards/create/", views.CreditCardCreate.as_view(), name="creditcard_create"),
	path("creditcards/<int:pk>/update/", views.CreditCardUpdate.as_view(), name="creditcard_update"),
	path("creditcards/<int:pk>/delete/", views.CreditCardDelete.as_view(), name="creditcard_delete"),
	path('profile/<int:profile_id>/add_creditcard/', views.add_creditcard, name='add_creditcard'),
	# path('profile/<int:profile_id>/add_creditcard/', views.add_creditcard, name='add_creditcard'),
	path("add_order/", views.add_order, name="add_order"),

	path("orders/", views.OrderList.as_view(), name="order_index"),
	path("orders/create/<int:shop_id>", views.OrderCreate.as_view(), name="order_start"),
	# path("orders/create/<int:shop_id>", views.start_order, name="order_start"),
	path("orders/<int:pk>/update/", views.OrderUpdate.as_view(), name="order_update"),
	path("orders/<int:pk>/delete/", views.OrderDelete.as_view(), name="order_delete"),
	path("orders/<int:pk>/", views.OrderDetail.as_view(), name="order_detail"),


	path("accounts/signup/", views.signup, name="signup"),
]