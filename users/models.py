from os import path
from typing import Tuple
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.urls import reverse


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     role = models.BooleanField(default=False)
#     image = models.ImageField(default = 'default2.jpg', upload_to = 'profile_pics')
#
#     def __str__(self):
#         return f'{self.user.username} Profile'
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         img = Image.open(self.image.path)
#
#         if img.height>300 or img.width>300:
#             output_size = (300,300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)

class User(AbstractUser):
    products = models.BooleanField(default = False)
    seller = models.BooleanField(default = False)
    image = models.ImageField(default = 'default2.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sellers')
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"users: {self.user.username}"

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='buyers')

    def __str__(self):
        return f"Buyer: {self.user.username}"