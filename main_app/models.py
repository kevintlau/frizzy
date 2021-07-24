from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.conf import settings
# Django built-in User Model from auth
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    address = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={ 'pk': self.id })

class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    # shop_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    city = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    delivery_fee = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={ 'pk': self.id })

class IceCream(models.Model):
    SIZES = (
        ('S', "Small"),
        ('M', "Medium"),
        ('L', "Large"),
        ('T', "Tub")
    )
    flavor = models.CharField(max_length=200)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    # icecream_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    description = models.TextField(max_length=400)
    promotion = models.DecimalField(max_digits=3, decimal_places=2)
    size = models.CharField(
        max_length=1,
        choices=SIZES,
        default=SIZES[0][0]
    )

    def __str__(self):
        return self.flavor

    def get_absolute_url(self):
        return reverse('icecream_detail', kwargs={ 'pk': self.id })

class CreditCard(models.Model):
    card_number = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    security_code = models.CharField(max_length=4)
    exp_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.card_number
    
    def get_absolute_url(self):
        return reverse('card_detail', kwargs={ 'pk': self.id })

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    icecreams = models.ManyToManyField(IceCream)

    def __str__(self):
        return f"{self.user} at {self.shop}"
    
    def get_absolute_url(self):
        return reverse('order_detail', kwargs={ 'pk': self.id })

