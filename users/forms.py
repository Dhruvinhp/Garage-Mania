from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from django import forms
from django.forms import fields
from .models import Seller, User, Buyer

# from .models import Profile
#
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#
# class Role(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['role']
#
# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username','email']
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']



# from django.contrib.auth.models import User
class SellerSignupForm(UserCreationForm):
    email = forms.CharField(max_length=200)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.seller = True
        user.email = self.cleaned_data.get('email')
        user.save()
        seller = Seller.objects.create(user=user)
        seller.save()
        # print(self.cleaned_data)
        return user

class BuyerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.buyer = True
        user.save()
        buyer = Buyer.objects.create(user=user)
        return buyer