from django.contrib import admin

from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "quantity", "expiry_date", "created_at")
    list_filter = ("category", "expiry_date")
    search_fields = ("name", "description", "category__name")
