from django.contrib import admin
from .models import Category, CarPart
from django.contrib.auth.models import Group

admin.site.site_header = "Garage Mania"

class CarPartAdmin(admin.ModelAdmin):
    list_display = ("part_name", "category", "seller", "is_new", "price", "date_posted")
    list_filter = ("seller", "date_posted")
    change_list_template = "admin/post/post_change_list.html"

admin.site.register(CarPart, CarPartAdmin)
admin.site.register(Category)
admin.site.unregister(Group)
