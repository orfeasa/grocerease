from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    # default user already has:
    # username, first_name, last_name, email, password
    # groups, user_permissions,
    # is_staff, is_active, is_superuser,
    # last_login, date_joined

    default_contingency = models.DecimalField(
        max_digits=3, decimal_places=2, default=0.1
    )
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(verbose_name="category name", max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"
        # one user cannot create more than one category with the same name
        unique_together = ["name", "user"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category-list")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s order placed {self.created_at}"


class Product(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    UNITS = (("ML", "ml"), ("G", "gram"), ("PC", "piece"))
    unit = models.CharField(max_length=2, choices=UNITS)

    estimated_daily_consumption = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True
    )
    estimation_certainty = models.DecimalField(
        max_digits=10, decimal_places=10, default=0.01, blank=True
    )
    details = models.CharField(max_length=512, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order}, {self.product} ({self.quantity})"
