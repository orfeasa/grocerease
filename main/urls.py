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
    path("categories/new/", views.CategoryCreateView.as_view(), name="category-create"),
    path("categories/", views.CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<int:pk>/edit/",
        views.CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path("orders/<int:pk>/edit/", views.OrderUpdateView.as_view(), name="order-update"),
    path(
        "orderitems/<int:pk>/edit",
        views.OrderItemUpdateView.as_view(),
        name="orderitem-update",
    ),
]
