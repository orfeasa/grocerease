from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from main import forms
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class PlanView(TemplateView):
    template_name = "main/plan.html"


class BaseView(TemplateView):
    template_name = "main/base.html"


class OrderView(TemplateView):
    template_name = "main/orders.html"
    # order list view


class IndexView(TemplateView):
    template_name = "main/index.html"


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
