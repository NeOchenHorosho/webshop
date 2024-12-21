from django.urls import path, include
from . import views

urlpatterns = [
path('signup/', views.SignUp.as_view(), name='signup'),
path('logout/', views.logout_view, name= 'logout'),
path('users/', include('django.contrib.auth.urls'))
]