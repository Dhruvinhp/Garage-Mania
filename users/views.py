from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .forms import RegisterForm
from .models import User #, Seller, Buyer
# from .forms import BuyerSignupForm, SellerSignupForm
from django.contrib.auth.decorators import login_required

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         role = request.POST.get("role", False)
#
#         if form.is_valid():
#             profile = form.save(commit=False)
#             print(role)
#             profile.user = request.user
#             profile.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"Account created for {username}, you are now able to Login!")
#
#             # # if role is seller
#             # if role:
#             #     profile.user.role = role
#             #     profile.user.save()
#             return redirect('login')
#
#
#         # if user.profile.role:
#         #     role = True
#         #     role.save()
#     else:
#         form = UserRegisterForm()
#         role = Role()
#
#     context = {
#         'form':form,
#         'role':role,
#     }
#     return render(request, 'users/register.html', context)
#
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f"Your Account has been updated!")
            return redirect("profile")
        else:
            return messages.warning(request, f"Something went wrong!")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }

    return render(request, "users/profile.html", context)


# class SellerSignupView(CreateView):
#     model = User
#     form_class = SellerSignupForm
#     template_name = "users/register.html"
#
#     # success_url = reverse_lazy('user_detail', kwargs={'pk':self.pk})
#     def get_success_url(self):
#         return reverse("car_parts:shop")
#
#
# class BuyerSignupView(CreateView):
#     model = Buyer
#     form_class = BuyerSignupForm
#     template_name = "users/register.html"
#
#     def get_success_url(self):
#         return reverse("car_parts: shop")

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "users/register.html"

    # success_url = reverse_lazy('user_detail', kwargs={'pk':self.pk})
    def get_success_url(self):
        return reverse("login")
