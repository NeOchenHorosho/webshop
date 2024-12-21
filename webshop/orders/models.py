from django.db import models
from users.models import CustomUser
from product.models import Product
from django.utils import timezone

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'В ожидании'),
        ('PROCESSING', 'В обработке'),
        ('COMPLETED', 'Завершен'),
        ('CANCELLED', 'Отменен'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.CharField(max_length=200, default= '')
    phone = models.CharField(max_length=13, default= '')
    def __str__(self):
        return f"Заказ #{self.id} от {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена на момент заказа

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"