from django.contrib import admin
from .views import (
    IndexView,
    ContactView,
    AboutView,
    # CarPartPurchaseView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ShowAllProducts,
)
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    # path("shop/", views.ShowAllProducts, name="shop"),
    path('shop/', ShowAllProducts.as_view(), name='shop'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("shop/<int:pk>/", PostDetailView.as_view(), name="shop-detail"),
    path("shop/new/", PostCreateView.as_view(), name="post-create"),
    path("shop/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("shop/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    # path("shop/<int:pk>/purchase", CarPartPurchaseView.as_view(), name="purchase"),
]
