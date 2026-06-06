from django.db import models
from django.urls import reverse

from foods.models import Food


class Order(models.Model):
    """Stores customer orders and the calculated price total."""
    customer_name = models.CharField(max_length=150)
    customer_phone = models.CharField(max_length=20)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-order_date"]

    def save(self, *args, **kwargs):
        """Always calculate total price on the server for accuracy."""
        self.total_price = self.food.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} - {self.food.name}"

    def get_absolute_url(self):
        return reverse("orders:list")
