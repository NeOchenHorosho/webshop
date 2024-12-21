from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'status', 'total']
    list_filter = ['status', 'created_at']
    inlines = [OrderItemInline]
admin.site.register(Order)