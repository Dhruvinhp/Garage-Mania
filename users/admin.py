from django.contrib import admin
from django.contrib.auth import models

# from .models import Profile
from .models import User
from django.contrib.auth.models import Group

# class ProfileAdmin(admin.ModelAdmin):
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('user', 'role', 'image')
#     list_filter = ('user',)
#     change_list_template = 'admin/profile/profile_change_list.html'

# admin.site.register(Profile, ProfileAdmin)
admin.site.register(User)
