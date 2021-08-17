from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm, ProfileUpdateForm
from .forms import RegisterForm, ProfileForm
from .models import User, Profile
from django.contrib.auth.decorators import login_required

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

class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "users/profile.html"

    def Post(request):
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


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "users/register.html"
    def get_success_url(self):
        return reverse("login")
