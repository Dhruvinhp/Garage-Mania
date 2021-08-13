from django.contrib import admin
from .models import User, Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')
    list_filter = ('user',)
    change_list_template = "admin/post/post_change_list.html"

admin.site.register(Profile, ProfileAdmin)
admin.site.register(User)
