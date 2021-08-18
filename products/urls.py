from django.contrib import admin
from .views import (
    IndexView,
    ContactView,
    AboutView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ShowAllProducts,
)
from . import views
from django.urls import path, include

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path('shop/', ShowAllProducts.as_view(), name='shop'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("shop/<int:pk>/", PostDetailView.as_view(), name="shop-detail"),
    path("shop/new/", PostCreateView.as_view(), name="post-create"),
    path("shop/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("shop/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("shop/<int:pk>/itemPurchase/", views.itemPurchase, name="itemPurchase"),
]
