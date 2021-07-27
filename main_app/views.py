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
from main_app.forms import SignUpForm
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
	return render(request, 'main_app/profile_detail.html')

class ProfileCreate(CreateView):
	model = Profile
	# what do we do about the user 1:1 relationship?
	fields = ["address", "phone_number"]
class ProfileUpdate(UpdateView):
	model = Profile
	fields = ["address", "phone_number"]
def add_creditcard(request, profile_id):
	pass
def assoc_order(request, profile_id, order_id):
	pass


class OrderList(ListView):
	model = Order
class OrderDetail(DetailView):
	model = Order
class OrderCreate(CreateView):
	model = Order
	fields = ["user_id", "shop_id", "creditcard_id"]
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
	success_url = "/creditcards/"


# SEE COMMENTS ON URLs FOR SHOP AND ICECREAM

# class ShopList(ListView):
# 	model = Shop
# class ShopDetail(DetailView):
# 	model = Shop
# class ShopCreate(CreateView):
# 	model = Shop
# class ShopUpdate(UpdateView):
# 	model = Shop
# class ShopDelete(DeleteView):
# 	model = Shop

# class IceCreamList(ListView):
# 	model = IceCream
# class IceCreamDetail(DetailView):
# 	model = IceCream
# class IceCreamCreate(CreateView):
# 	model = IceCream
# class IceCreamUpdate(UpdateView):
# 	model = IceCream
# class IceCreamDelete(DeleteView):
# 	model = IceCream



# @login_required
# def add_feeding(request, cat_id):
#   # instantiate a new form object using the key-value pairs from the post req
#   form = FeedingForm(request.POST)
#   # check if the inputs are valid
#   if form.is_valid():
#     # create in-memory representation of the form object
#     new_feeding = form.save(commit=False)
#     new_feeding.cat_id = cat_id
#     new_feeding.save()
#   return redirect("cats_detail", cat_id=cat_id)

# # @login_required
# def assoc_toy(request, cat_id, toy_id):
#   Cat.objects.get(id=cat_id).toys.add(toy_id)
#   return redirect("cats_detail", cat_id=cat_id)

# @login_required
# def cats_detail(request, cat_id):
#   cat = Cat.objects.get(id=cat_id)
#   # check if cat's user is the actual owner
#   if cat.user != request.user:
#     return redirect("cats_index")
#   # get the toys that the cat doesn't have
#   unowned_toys = Toy.objects.exclude(
#     # exclude all toys where the toy id is within the cat's list of owned toys
#     # note the double underscore in "id__in"
#     id__in=cat.toys.all().values_list("id")
#   )
#   # instantiate feeding form to be rendered in template
#   feeding_form = FeedingForm()
#   return render(request, "cats/detail.html", { 
#     "cat": cat,
#     "feeding_form": feeding_form,
#     # add toys to be displayed in selector list
#     "unowned_toys": unowned_toys,
#   })
