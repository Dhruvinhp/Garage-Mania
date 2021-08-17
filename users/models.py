from os import path
from typing import Tuple
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from PIL import Image

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
