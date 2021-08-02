from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView,
    DeleteView,
)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'buyer/shop.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'buyer/shop.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'buyer/shop_detail.html'

class IndexView(ListView):
    model = Post
    template_name = 'buyer/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class ContactView(ListView):
    model = Post
    template_name = 'buyer/contact.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class AboutView(ListView):
    model = Post
    template_name = 'buyer/about.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin, CreateView): #here we use Create View
    model = Post
    fields = ['part_name', 'brand', 'car_model_name', 'category', 'description', 'is_new', 'image', 'prize']
    template_name = 'buyer/shop_form.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #here we use update View
    model = Post
    fields = ['part_name', 'brand', 'car_model_name', 'category', 'description', 'is_new', 'image', 'prize']
    template_name = 'buyer/shop_form.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #here we use Delete View
    model = Post
    success_url = '/' 
    template_name = 'buyer/shop_form.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False
