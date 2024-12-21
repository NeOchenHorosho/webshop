from django.urls import path
from .views import CheckoutView, OrderListView, OrderDetailView


urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('my-orders/', OrderListView.as_view(), name='order_list'),
    path('order/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
]