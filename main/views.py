import datetime

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
    model = Order
    context_object_name = "orders"
    template_name = "main/orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.datetime.now()
        return context

    def get_queryset(self):
        return super().get_queryset()


class IndexView(TemplateView):
    template_name = "main/index.html"


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
