from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_phone", "food", "quantity", "total_price", "order_date")
    list_filter = ("order_date", "food")
    search_fields = ("customer_name", "customer_phone", "food__name")
    readonly_fields = ("total_price", "order_date")
