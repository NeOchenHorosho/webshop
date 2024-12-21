from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from .forms import OrderForm
from cart.models import Cart, CartItem
from .models import Order, OrderItem

class CheckoutView(LoginRequiredMixin, View):
    template_name = 'order/checkout.html'
    
    def get(self, request, *args, **kwargs):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        
        if not cart_items.exists():
            messages.error(request, "Ваша корзина пуста.")
            return redirect('home') 
        form= OrderForm(request.GET)
        context = {
            'cart_items': cart_items
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        
        if not cart_items.exists():
            messages.error(request, "Ваша корзина пуста.")
            return redirect('cart_detail')
        form = OrderForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            with transaction.atomic():
                order = Order.objects.create(
                    user=user,
                    status='PENDING',
                    address=address,
                    phone=phone
                )
                total = 0
                order_items = []
                for item in cart_items:
                    order_item = OrderItem(
                        order=order,
                        product=item.product,
                        quantity=item.quantity,
                        price=item.product.price
                    )
                    order_items.append(order_item)
                    total += item.product.price * item.quantity
                OrderItem.objects.bulk_create(order_items)
                order.total = total
                order.save()

                cart_items.delete()

                messages.success(request, f"Заказ #{order.id} успешно оформлен.")
                return redirect('order_detail', order_id=order.id)

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10  

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)