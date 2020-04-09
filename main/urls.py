from django.urls import path
from . import views

urlpatterns = [
    path("plan/", views.PlanView.as_view(), name="plan"),
    path("base/", views.BaseView.as_view(), name="base"),
]
