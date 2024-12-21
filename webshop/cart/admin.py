from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1 
    can_delete = True 

class CartAdmin(admin.ModelAdmin): 
    list_display = ('user', 'id') 
    search_fields = ('user__username', 'user__email')
    inlines = [CartItemInline]

admin.site.register(Cart, CartAdmin)
