from django.contrib import admin
from .views import (
    IndexView, PostListView, ContactView, AboutView, 
    PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
)
from . import views as user_views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('home/', IndexView.as_view(), name='buyer-home'),
    path('shop/', PostListView.as_view(), name='buyer-shop'),
    path('contact/', ContactView.as_view(), name='buyer-contact'),
    path('about/', AboutView.as_view(), name='buyer-about'),
    path('shop-single/', PostDetailView.as_view(), name='shop-single'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
