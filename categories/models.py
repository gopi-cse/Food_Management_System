from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Stores food groups such as Fruits, Dairy, Bakery, or Beverages."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories:list")
