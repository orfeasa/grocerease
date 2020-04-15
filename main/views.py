from django.shortcuts import render
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

class LoginView(TemplateView):
    template_name = "main/login.html"


class RegisterView(TemplateView):
    template_name = "main/register.html"