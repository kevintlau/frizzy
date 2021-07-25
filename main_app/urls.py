from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path("about/", views.about, name="about"),
	path("search_shops/", views.search_shops, name="search_shops"),

	# path("profile/<int:pk>/", views.ProfileDetail.as_view(), name="profile_detail"),
	path("profile/", views.profile, name="profile_detail"),
	path("profile/create/", views.ProfileCreate.as_view(), name="profile_create"),
	path("profile/<int:pk>/update/", views.ProfileUpdate.as_view(), name="profile_update"),
	path("profile/<int:pk>/add_creditcard/", views.add_creditcard, name="add_creditcard"),
	path("profile/<int:profile_pk>/assoc_order/<int:order_pk>/", views.assoc_order, name="assoc_order"),

	path("creditcards/", views.CreditCardDetail.as_view(), name="creditcard_index"),
	# TEST: add profile_pk here so the form can know which user to link the new card to
	path("creditcards/create/", views.CreditCardCreate.as_view(), name="creditcard_create"),
	path("creditcards/<int:pk>/update/", views.CreditCardUpdate.as_view(), name="creditcard_update"),
	path("creditcards/<int:pk>/delete/", views.CreditCardDelete.as_view(), name="creditcard_delete"),

	path("orders/", views.OrderList.as_view(), name="order_index"),
	# blank view with a button that submits a form to prepopulate user pk and store pk
	path("orders/create/<int:user_pk>/<int:shop_pk>/", views.OrderCreate.as_view(), name="order_create"),
	# update for creditcard selection
	path("orders/<int:pk>/update/", views.OrderUpdate.as_view(), name="order_update"),
	path("orders/<int:pk>/delete/", views.OrderDelete.as_view(), name="order_delete"),
	path("orders/<int:pk>/", views.OrderDetail.as_view(), name="order_detail"),


	# shops CRUD for admins - need to find a way to authorize
	# alternatively, don't even make urls and views for this feature, since it's not user-facing
	# path("shops/", views.ShopList.as_view(), name="shop_index"),
	# path("shops/create/", views.ShopCreate.as_view(), name="shop_create"),
	# path("shops/<int:pk>/add_icecream/", views.add_icecream, name="add_icecream"),
	# path("shops/<int:pk>/update/", views.ShopUpdate.as_view(), name="shop_update"),
	# # do we need a shop deletion?
	# # path("shops/<int:pk>/delete/", views.ShopDelete.as_view(), name="shop_delete"),
	# path("shops/<int:pk>/", views.ShopDetail.as_view(), name="shop_detail"),

	# same idea as with shops - we might not need this yet, since it's not user-facing
	# path("icecream/", views.IceCreamList.as_view(), name="icecream_index"),
	# path("icecream/<int:pk>/", views.IceCreamDetail.as_view(), name="icecream_detail"),
	# path("icecream/create/", views.IceCreamCreate.as_view(), name="icecream_create"),
	# path("icecream/<int:pk>/update/", views.IceCreamUpdate.as_view(), name="icecream_update"),
	# path("icecream/<int:pk>/delete/", views.IceCreamDelete.as_view(), name="icecream_delete"),

	path("accounts/signup/", views.signup, name="signup"),
]