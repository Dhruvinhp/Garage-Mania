from django.contrib import admin
from .models import Category, Post
from django.contrib.auth.models import Group


admin.site.site_header = "Garage Mania"

class PostAdmin(admin.ModelAdmin):
    list_display = ('part_name', 'category', 'seller', 'is_new', 'prize','date_posted')
    list_filter = ('seller','date_posted')
    change_list_template = 'admin/post/post_change_list.html'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.unregister(Group)