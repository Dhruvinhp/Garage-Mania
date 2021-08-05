from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Category, Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView,
    DeleteView,
)
from django.conf import settings
from .forms import AddPart

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'buyer/shop.html', context)

def ShowAllProducts(request):
    category = request.GET.get('category')
    
    if category == None:
        parts = Post.objects.order_by('-prize')
        page_num = request.GET.get("page")
        paginator = Paginator(parts, 6)
        try:
            parts = paginator.page(page_num)
        except PageNotAnInteger:
            parts = paginator.page(1)
        except EmptyPage:
            parts = paginator.page(paginator.num_pages)  
    else:
        parts = Post.objects.filter(category__name = category)

    categories = Category.objects.all()
    context = {
        'posts' : parts,
        'categories' : categories
    }
    return render(request, 'buyer/shop.html', context)

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
    form_class = AddPart
    # fields = ['part_name', 'brand', 'car_model_name', 'category', 'description', 'is_new', 'image', 'prize']
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
    success_url = '/shop'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False

def sendEmail(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    subject = 'Garage Mania Order Received!'
    message = f"Your Item has been purchased by {user.username}, Buyer's details: Emailid: {user.email}, Order Details - Part Name: {post.part_name}, Prize: {post.prize} Rs. "
    sender = settings.EMAIL_HOST_USER
    receiver = {post.seller.email}
    print(message)
    send_mail(
        subject, message, sender, receiver, 
        fail_silently=False
    )
    return render(request, 'buyer/order_confirm.html')