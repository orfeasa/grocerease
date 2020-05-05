from django import forms as djangoforms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from main import forms
from main.models import Category, Order, OrderItem


class PlanView(LoginRequiredMixin, TemplateView):
    template_name = "main/plan.html"


class OrderListView(LoginRequiredMixin, ListView):
    template_name = "main/order_list.html"

    def get_queryset(self):
        # only show orders of that user in descending creation date
        return Order.objects.filter(user=self.request.user).order_by("-created_at")


class IndexView(TemplateView):
    template_name = "main/index.html"


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name_suffix = "_create_form"
    fields = ["name"]

    def form_valid(self, form):
        # set the current user as the user of this category
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "main/category_list.html"

    def get_queryset(self):
        # only show categories of that user in descending name
        return Category.objects.filter(user=self.request.user).order_by("name")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ["name"]
    template_name_suffix = "_update_form"


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name_suffix = "_confirm_delete"
    success_url = reverse_lazy("category-list")

class OrderItemUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderItem
    fields = ["product", "quantity"]
    template_name_suffix = "_update_form"
