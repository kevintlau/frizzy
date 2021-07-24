from django.contrib import admin
from .models import Profile
from .models import Shop
from .models import IceCream
from .models import CreditCard
from .models import Order

# Register your models here.

admin.site.register(Profile)
admin.site.register(Shop)
admin.site.register(IceCream)
admin.site.register(CreditCard)
admin.site.register(Order)