from typing import List
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import (
	CreateView, 
	UpdateView, 
	DeleteView, 
	ListView, 
	DetailView
)
from .models import Profile, CreditCard, Order, Shop, IceCream
from django.db.models import Q
# from .forms import 
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from main_app.forms import SignUpForm, CreditCardForm
from main_app.forms import OrderForm
# decorator to enforce login for view functions
from django.contrib.auth.decorators import login_required
# class-based views require a mixin - classes can't have decorators
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

# basic homepage
def home(request):
	return render(request, "home.html")

def about(request):
	return render(request, "about.html")

def signup(request):
	error_message = ""
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			# load the profile instance created by the signal
			user.refresh_from_db()
			user.profile.address = form.cleaned_data.get('address')
			user.profile.phone_number = form.cleaned_data.get('phone_number')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect("profile_detail")
		else:
			error_message = "Invalid signup data - please try again"
	form = SignUpForm()
	return render(request, "registration/signup.html", { 
    	"form": form,
    	"error_message": error_message,
  	})

class SearchResultsView(ListView):
	model = Shop
	template_name = "search_shops.html"

	def get_queryset(self):
		query = self.request.GET.get("search")
		object_list = Shop.objects.filter(
			Q(name__icontains=query) | Q(city__icontains=query)
		)
		return object_list

def shop_details(request, shop_id):
	shop = Shop.objects.get(id=shop_id)
	flavors = IceCream.objects.filter(shop_id=shop_id)
	order = Order.objects.all()
	form = OrderForm()
	return render(request, 'main_app/shop_detail.html', {'shop': shop, 'flavors': flavors, 'order': order, 'form': form})

# def search_shops(request):
# 	if request.method == "POST":
# 		searched = UserCreationForm(request.POST)
# 		if searched.is_valid():
# 			user = searched.save()
# 			login(request, user)
# 			shop = Shop.objects.filter(name__contains= searched)
# 			return render(request, 'search_shops.html',
# 			{'searched':searched, 
# 			'shop':shop})
# 		else:
# 			error_message = "Invalid search - please try again" 
# 			return render(request, "registration/signup.html", { 
#     		"form": form,
#     		"error_message": error_message,
# 			})


class ProfileList(ListView):
	model = Profile
# class ProfileDetail(DetailView):
# 	model = Profile
def profile(request):
	creditcard_form = CreditCardForm()
	return render(request, 'main_app/profile_detail.html', { 
		'creditcard_form':creditcard_form
	})
	

class ProfileCreate(CreateView):
	model = Profile
	# what do we do about the user 1:1 relationship?
	fields = ["address", "phone_number"]
class ProfileUpdate(UpdateView):
	model = Profile
	fields = ["address", "phone_number"]


def add_creditcard(request, profile_id):
	form = CreditCardForm(request.POST)
	if form.is_valid():
		new_creditcard = form.save(commit=False)
		new_creditcard.profile_id = profile_id
		new_creditcard.save()
	return redirect('profile_detail')

def add_order(request, shop_id):
	form = OrderForm(request.POST)
	if form.is_valid():
		new_order = form.save(commit=False)
		new_order.shop_id = shop_id
		new_order.save()
	return redirect('shop_detail', shop_id=shop_id)

class OrderList(ListView):
	model = Order
class OrderDetail(DetailView):
	model = Order

class OrderUpdate(UpdateView):
	model = Order
	fields = ["creditcard_id"]
class OrderDelete(DeleteView):
	model = Order
	success_url = "/orders/"


class CreditCardList(ListView):
	model = CreditCard
class CreditCardDetail(DetailView):
	model = CreditCard
class CreditCardCreate(CreateView):
	model = CreditCard
	fields = "__all__"
class CreditCardUpdate(UpdateView):
	model = CreditCard
	fields = ["card_number", "security_code", "exp_date"]
class CreditCardDelete(DeleteView):
	model = CreditCard
	success_url = "/profile/"