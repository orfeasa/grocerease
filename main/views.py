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
from main.forms import CategoryForm
from main.models import Order


class PlanView(LoginRequiredMixin, TemplateView):
    template_name = "main/plan.html"


class OrderListView(LoginRequiredMixin, ListView):
    context_object_name = "orders"
    template_name = "main/orders.html"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class IndexView(TemplateView):
    template_name = "main/index.html"


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
