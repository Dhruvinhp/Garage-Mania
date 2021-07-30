from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone
from PIL import Image

from django.urls import reverse

# Create your models here.
class Post(models.Model):
    CATEGORY_TYPE ={
        ('E','Engine'),
        ('FS','Fuel system'),
        ('EX_S','Exhaust system'),
        ('CS','Cooling system'),
        ('LS','Lubrication system'),
        ('EL_S','Electrical system'),
        ('T','Transmission'),
        ('C','Chassis'),
    }
    part_name = models.CharField(max_length=32, null=True)
    car_model_name = models.CharField(max_length=32, null=True)
    brand = models.CharField(max_length=32, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_TYPE, null=True)
    description = models.TextField()
    is_new = models.BooleanField(default=False)
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'parts_pics')
    prize = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.part_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk':self.pk})