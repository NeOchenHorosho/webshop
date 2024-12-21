from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product
from users.models import CustomUser
from .models import Cart, CartItem
from django.views.generic import TemplateView


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_id)
        
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
        
        return redirect('home')

class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, iscreated = Cart.objects.get_or_create(user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart).select_related('product')
        context['cart_items'] = cart_items
        context['total'] = sum(item.product.price * item.quantity for item in cart_items)
        return context

class UpdateCartItemView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        cart_item_id = self.kwargs.get('item_id')
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        
        return redirect('cart')

class DeleteCartItemView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        cart_item_id = self.kwargs.get('item_id')
        cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
        cart_item.delete()
        return redirect('cart')