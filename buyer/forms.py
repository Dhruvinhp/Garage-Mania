from django import forms
from django.forms import fields
from .models import Post

class AddPart(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['part_name', 'brand', 'car_model_name' , 'category', 'description', 'is_new' , 'image', 'prize']