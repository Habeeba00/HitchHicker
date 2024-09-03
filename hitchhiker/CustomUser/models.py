from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractUser


class CustomUser(AbstractUser,PermissionsMixin):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,unique=True)
    email=models.EmailField(unique=True)
    phone=models.IntegerField()
    is_staff=models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)


