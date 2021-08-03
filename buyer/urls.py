from django.contrib import admin
from .views import (
    IndexView, ContactView, AboutView, 
    PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
)
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('shop/', views.ShowAllProducts, name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('shop/<int:pk>/', PostDetailView.as_view(), name='shop-detail'),
    path('shop/new/', PostCreateView.as_view(), name='post-create'),
    path('shop/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('shop/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('sendEmail/', views.sendEmail, name='sendEmail'),
]
