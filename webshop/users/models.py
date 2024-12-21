from django.db import models

from django.contrib.auth.models import  AbstractUser


class CustomUser(AbstractUser):
    user_balance= models.DecimalField(max_digits=10, decimal_places=2, default=0)
