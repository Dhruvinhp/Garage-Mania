from os import path
from typing import Tuple
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.urls import reverse

# class User(AbstractUser):
#     products = models.BooleanField(default=False)
#     seller = models.BooleanField(default=False)
#     image = models.ImageField(default="default2.jpg", upload_to="profile_pics")
#
#     def __str__(self):
#         return self.username
#
#     def get_absolute_url(self):
#         return reverse("user_detail", kwargs={"pk": self.pk})
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         img = Image.open(self.image.path)
#
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
#
#
# class Seller(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Seller")
#     address = models.CharField(max_length=200, null=True, blank=True)
#
#     def __str__(self):
#         return f"users: {self.user.username}"
#
#
# class Buyer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Buyer")
#
#     def __str__(self):
#         return f"Buyer: {self.user.username}"
class User(AbstractUser):
    SELLER = 0
    BUYER = 1

    USER_TYPE = (
        (SELLER, "Seller"),
        (BUYER, "Buyer")
    )

    user_role = models.IntegerField(choices=USER_TYPE, default=BUYER)
    phone_number = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default2.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
