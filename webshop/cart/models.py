from django.db import models
from product.models import Product
from users.models import CustomUser
from django.utils import timezone

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username +"'s cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.product.name + " items"

