from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone
from PIL import Image
# from users.models import Buyer
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.name

class CarPart(models.Model):
    part_name = models.CharField(max_length=32, null=True)
    brand = models.CharField(max_length=32, null=True)
    car_model_name = models.CharField(max_length=32, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    is_new = models.BooleanField(default=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'parts_pics')
    prize = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now) 

    class Meta:
        ordering = ["-prize"]
 
    def __str__(self):
        return self.part_name

    def get_absolute_url(self):
        return reverse('shop-detail', kwargs={'pk':self.pk})

class Purchase(models.Model):
    car_part = models.ForeignKey(CarPart, on_delete=models.CASCADE)
    # products = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car_part}" # is purchased by products {self.products}"
