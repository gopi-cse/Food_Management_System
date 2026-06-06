"""General website pages and the authenticated dashboard."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from categories.models import Category
from foods.models import Food
from orders.models import Order


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        """Add dashboard numbers and recent records to the template."""
        context = super().get_context_data(**kwargs)
        context["total_foods"] = Food.objects.count()
        context["total_categories"] = Category.objects.count()
        context["total_orders"] = Order.objects.count()
        context["recent_orders"] = Order.objects.select_related("food")[:5]
        context["low_stock_foods"] = Food.objects.select_related("category").filter(quantity__lte=5)[:5]
        return context
