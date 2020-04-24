from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("plan/", views.PlanView.as_view(), name="plan"),
    path("orders/", views.OrderListView.as_view(), name="orders-list"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout", kwargs={"next_page": "/"}),
    path("", views.IndexView.as_view(), name="index"),
]
