from django.urls import path
from . import views

urlpatterns = [
    path("plan/", views.PlanView.as_view(), name="plan"),
    path("orders/", views.OrderView.as_view(), name="orders"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.LoginView.as_view(), name="register"),
]
