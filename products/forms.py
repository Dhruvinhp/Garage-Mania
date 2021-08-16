# from .models import Seller, User, CarPart, Buyer
from django import forms
from .models import CarPart

class CarPartForm(forms.ModelForm):
    class Meta:
        model = CarPart
        fields = [
            "part_name",
            "car_model_name",
            "brand",
            "category",
            "description",
            "quality",
        ]
