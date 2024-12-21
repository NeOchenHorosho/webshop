from django.urls import path
from .views import AddToCartView, CartView, UpdateCartItemView, DeleteCartItemView

urlpatterns = [
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/update/<int:item_id>/', UpdateCartItemView.as_view(), name='update_cart_item'),
    path('cart/delete/<int:item_id>/', DeleteCartItemView.as_view(), name='delete_cart_item'),
]