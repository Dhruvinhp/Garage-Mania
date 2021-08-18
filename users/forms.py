from django.contrib.auth.forms import UserCreationForm, UserModel
from django.db import transaction
from django import forms
from .models import User, Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class RegisterForm(UserCreationForm):
    email = forms.CharField(max_length=200)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2','phone_number','address','user_role')

    @transaction.atomic
    def save(self):
        userRegister = super().save(commit=False)
        userRegister.email = self.cleaned_data.get("email")
        userRegister.save()
        return userRegister