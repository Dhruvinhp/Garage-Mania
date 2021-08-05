from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Role, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        role = Role(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}, you are now able to Login!")
            return redirect('login')
    else:
        form = UserRegisterForm()
        role = Role()

    context={
        'form' : form,
        'role': role,
    }
    return render(request, 'Seller/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
        else:
            return messages.warning(request, f'Something went wrong!')
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        role = Role(instance=request.user.profile)

    context = {
         'u_form':u_form,
         'p_form':p_form,
         'role':role,
    }

    return render(request, 'Seller/profile.html', context)