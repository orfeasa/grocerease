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
