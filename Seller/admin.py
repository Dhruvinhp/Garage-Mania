from django.contrib import admin
from django.contrib.auth import models
from .models import Profile
from django.contrib.auth.models import Group

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'image')
    list_filter = ('user',)
    change_list_template = 'admin/profile/profile_change_list.html'

admin.site.register(Profile, ProfileAdmin)