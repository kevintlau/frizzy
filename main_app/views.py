from typing import List
from django.http import request
from django.http.response import HttpResponse
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
		if not query :
			query = ""
		object_list = Shop.objects.filter(
			Q(name__icontains=query) | Q(city__icontains=query)
		)
		return object_list

class ShopList(ListView):
	model = Shop

def shop_details(request, shop_id):
	shop = Shop.objects.get(id=shop_id)
	flavors = IceCream.objects.filter(shop_id=shop_id)
	order = Order.objects.all()
	form = OrderForm()
	return render(request, 'main_app/shop_detail.html', {'shop': shop, 'flavors': flavors, 'order': order, 'form': form})

@login_required
def profile(request):
	creditcard_form = CreditCardForm()
	return render(request, 'main_app/profile_detail.html', { 
		'creditcard_form':creditcard_form
	})
	
# TODO: add profile updating
class ProfileUpdate(UpdateView):
	model = Profile
	fields = ["address", "phone_number"]

@login_required
def add_creditcard(request, profile_id):
	form = CreditCardForm(request.POST)
	if form.is_valid():
		new_creditcard = form.save(commit=False)
		new_creditcard.profile_id = profile_id
		new_creditcard.save()
	return redirect('profile_detail')

class OrderList(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Order.objects.filter(user_id=self.request.user.id)

class OrderDetail(LoginRequiredMixin, DetailView):
	model = Order

class OrderCreate(LoginRequiredMixin, CreateView):
	model = Order
	# fields = "__all__"
	fields = ['icecreams','creditcard']
	success_url = "/orders/"

	# custom form validator to add user and shop ids
	def form_valid(self, form):
		new_order = form.save(commit=False)
		new_order.user_id = self.request.user.id
		# grab shop ID from URL
		new_order.shop_id = self.request.resolver_match.kwargs['shop_id']
		new_order.save()
		return super().form_valid(form)

@login_required
def start_order(request, shop_id):
	flavors = IceCream.objects.filter(shop_id=shop_id)
	creditcards = CreditCard.objects.filter(profile_id=request.user.profile.id)
	return render(request, "main_app/order_form.html", {
		"shop_id": shop_id, 
		"user_id": request.user.id,
		"flavors": flavors,
		"creditcards": creditcards,
	})


class OrderUpdate(LoginRequiredMixin, UpdateView):
	model = Order
	fields = ["icecreams", "creditcard"]
class OrderDelete(LoginRequiredMixin, DeleteView):
	model = Order
	success_url = "/orders/"


class CreditCardUpdate(LoginRequiredMixin, UpdateView):
	model = CreditCard
	fields = ["card_number", "security_code", "exp_date"]
class CreditCardDelete(LoginRequiredMixin, DeleteView):
	model = CreditCard
	success_url = "/profile/"