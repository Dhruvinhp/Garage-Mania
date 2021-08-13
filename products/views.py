from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Category, CarPart #Purchase
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.conf import settings


# def ShowAllProducts(request):
#     category = request.GET.get("category")
#
#     if category == None:
#         parts = CarPart.objects.order_by("-prize")
#         page_num = request.GET.get("page")
#         paginator = Paginator(parts, 6)
#         try:
#             parts = paginator.page(page_num)
#         except PageNotAnInteger:
#             parts = paginator.page(1)
#         except EmptyPage:
#             parts = paginator.page(paginator.num_pages)
#     else:
#         parts = CarPart.objects.filter(category__name=category)
#
#     categories = Category.objects.all()
#     context = {"posts": parts, "categories": categories}
#     return render(request, "products/shop.html", context)

class ShowAllProducts(ListView):
    model = CarPart
    template_name = 'products/shop.html'
    paginate_by = 6

    # def get_queryset(self):
    #     return Post.objects.filter(category = 1)
    # def get(self, request):
    #     category_name = Category.objects.all()
    #     parts = CarPart.objects.filter(category=category_name)
    #     context = {
    #         'posts':parts,
    #     }
    #     return render(request, self.template_name, context)

    def post(self, request):
        category_name = request.POST.get('category', None)
        parts = CarPart.objects.filter(category=category_name)
        context = {
                'posts':parts,
            }
        return render(request, self.template_name, context)

# def get_queryset(self):
#     return super().get_queryset()
#     # return Post.objects.filter(category=name)
#
# def post(self, request):
#     category_name = request.POST.get('category_name', None)
#     parts = Post.objects.filter(category=category_name)
#     categories = category.objects.all()
#     context = {
#             'posts':parts,
#             'categories': categories,
#         }
#     return render(request, self.template_name, context)


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
        "is_new",
        "prize",
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
        "is_new",
        "image",
        "prize",
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
    LoginRequiredMixin, UserPassesTestMixin, DeleteView
):  # here we use Delete View
    model = CarPart
    success_url = "/shop"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False


# def sendEmail(request, pk):
#     post = Post.objects.get(pk=pk)
#     user = request.user
#     subject = 'Garage Mania Order Received!'
#     message = f"Your Item has been purchased by {user.username}, Buyer's details: Emailid: {user.email}, Order Details - Part Name: {post.part_name}, Prize: {post.prize} Rs. "
#     sender = settings.EMAIL_HOST_USER
#     receiver = {post.seller.email}
#     print(message)
#     send_mail(
#         subject, message, sender, receiver,
#         fail_silently=False
#     )
#     return render(request, 'products/order_confirm.html')


# class CarPartPurchaseView(View):
#     def post(self, request, *args, **kwargs):
#         # add entry in purchase
#         car_part_pk = kwargs.get("pk")
#         car_part = CarPart.objects.get(pk=car_part_pk)
#         po = Purchase.objects.create(car_part=car_part, buyer=request.user.buyer)
#
#         # send mail to seller
#         subject = "Garage Mania | Order Received"
#         message = f"Your Item has been purchased by {user.username}, Buyer's details: Emailid: {user.email}, Order Details - Part Name: {post.part_name}, Prize: {post.prize} Rs. "
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [car_part.seller.user.email]
#         send_mail(subject, message, email_from, recipient_list)
#
#         if po:
#             msg = "Purchased successfully."
#         else:
#             msg = "Something went wrong! order not placed"
#         context = {"msg": msg}
#         return render(request, "products/order_confirm.html", context)
