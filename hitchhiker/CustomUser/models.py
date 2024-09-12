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
    is_owner=models.BooleanField(default=False)




class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=255)
    expiration_date = models.DateTimeField()




class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items_for_otp = []

        for i in range(6):
            num = random.choice(number_list)
            code_items_for_otp.append(num)

        code_string = "".join(str(item) for item in code_items_for_otp)
        self.otp = code_string
        super().save(*args, **kwargs)


# class BlacklistToken(models.Model):
#     token = models.CharField(max_length=255, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.token

