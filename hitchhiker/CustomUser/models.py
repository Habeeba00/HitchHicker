from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractUser
import random



class CustomUser(AbstractUser,PermissionsMixin):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(max_length=30,unique=True)
    email=models.EmailField(unique=True)
    phone=models.IntegerField()
    is_staff=models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)

    otp = models.CharField(
        max_length=6, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items_for_otp = []

        for i in range(6):
            num = random.choice(number_list)
            code_items_for_otp.append(num)

        code_string = "".join(str(item)
                              for item in code_items_for_otp) 
        self.otp = code_string
        super().save(*args, **kwargs)


