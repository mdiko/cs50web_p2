from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse


class User(AbstractUser):
    email = models.EmailField(("email address"), blank=True, primary_key=True)
    pass

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)

    category_list = (
        'Antiques'
        'Art',
        'Baby',
        'Books',
        'Business & Industrial',
        'Cameras & Photo',
        'Cell Phones & Accessories',
        'Clothing, Shoes & Accessories',
        'Coins & Paper Money',
        'Collectibles',
        'Computers/Tablets & Networking',
        'Consumer Electronics',
        'Crafts',
        'Dools & Bears',
        'Entertainment Memorabilia',
        'Home & Garden',
        'Motors',
        'Pet Supplies',
        'Sporting Goods',
        'Sports Mem, Cards & Fan Shop',
        'Toys & Hobbies',
        'Other'
    )

    category = models.CharField(max_length=25)

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.name

class Listing(models.Model):
    id = models.BigAutoField(primary_key=True)
    title =  models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing")
    startingbid = models.FloatField(max_length=10, default=0, blank=True)
    image_url = models.URLField(verbose_name="Image URL", blank=True)
    availibility = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, max_length=80, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listing-detail', kwargs={'pk': self.pk})

class Bid(models.Model):
    id = models.BigAutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None, related_name="bid")
    bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=500)
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return f"{self.author} commented: {self.text}"
