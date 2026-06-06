from django.db import models
from django.urls import reverse

from categories.models import Category


class Food(models.Model):
    """Represents an inventory item that can be ordered."""
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="foods")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    expiry_date = models.DateField()
    image = models.ImageField(upload_to="food_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("foods:list")
