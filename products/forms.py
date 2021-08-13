# from .models import Seller, User, CarPart, Buyer
from django import forms
from .models import CarPart
#
#
# # from django.contrib.auth.models import User
# class SellerSignupForm(UserCreationForm):
#     email = forms.CharField(max_length=200)
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_seller = True
#         user.email = self.cleaned_data.get("email")
#         user.save()
#         seller = Seller.objects.create(user=user)
#         seller.save()
#         # print(self.cleaned_data)
#         return user
#
#
# class BuyerSignupForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.buyer = True
#         user.save()
#         buyer = Buyer.objects.create(user=user)
#         return buyer


class CarPartForm(forms.ModelForm):
    class Meta:
        model = CarPart
        fields = [
            "part_name",
            "car_model_name",
            "brand",
            "category",
            "description",
            "is_new",
        ]
