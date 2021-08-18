from django.shortcuts import render, redirect
from .models import Category, CarPart #, Purchase
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.conf import settings

class ShowAllProducts(ListView):
    model = CarPart
    template_name = 'products/shop.html'
    paginate_by = 6
    ordering = ['price']

    def get(self, request):
        category_name = request.GET.get('category_name', None)
        if category_name == None:
            parts = CarPart.objects.all()
        else:
            parts = CarPart.objects.filter(category=category_name)

        categories = Category.objects.all()
        context = {
            "posts": parts,
            "categories": categories
        }
        return render(request, self.template_name, context)

class PostDetailView(DetailView):
    model = CarPart
    template_name = "products/shop_detail.html"

class IndexView(ListView):
    model = CarPart
    template_name = "products/index.html"
    context_object_name = "posts"


class ContactView(ListView):
    model = CarPart
    template_name = "products/contact.html"
    context_object_name = "posts"


class AboutView(ListView):
    model = CarPart
    template_name = "products/about.html"
    context_object_name = "posts"


class PostCreateView(LoginRequiredMixin, CreateView):  # here we use Create View
    model = CarPart
    fields = [
        "part_name",
        "brand",
        "car_model_name",
        "category",
        "description",
        "quality",
        "price",
        "image",
    ]
    template_name = "products/shop_form.html"

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class PostUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):  # here we use update View
    model = CarPart
    fields = [
        "part_name",
        "brand",
        "car_model_name",
        "category",
        "description",
        "quality",
        "image",
        "price",
    ]
    template_name = "products/shop_form.html"

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False


class PostDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CarPart
    success_url = "/shop"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False


def itemPurchase(request, pk):
    post = CarPart.objects.get(pk=pk)
    user = request.user
    subject = 'Garage Mania | Order Received!'
    message = f"Your Item has been purchased by {user.username}, Buyer's details: Email id: {user.email}, Phone number: {user.phone_number}, Order Details - Part Name: {post.part_name}, Prize: {post.price} Rs. "
    sender = settings.EMAIL_HOST_USER
    receiver = {post.seller.email}
    print(message)
    send_mail(
        subject, message, sender, receiver,
        fail_silently=False
    )
    return render(request, 'products/order_confirm.html')