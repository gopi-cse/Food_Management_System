from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import OrderForm
from .models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.select_related("food", "food__category")


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("orders:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["food_prices"] = {str(food.id): str(food.price) for food in self.form_class.base_fields["food"].queryset}
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        food = self.object.food
        food.quantity -= self.object.quantity
        food.save(update_fields=["quantity"])
        messages.success(self.request, "Order created and total price calculated successfully.")
        return response


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("orders:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["food_prices"] = {str(food.id): str(food.price) for food in self.form_class.base_fields["food"].queryset}
        return context

    def form_valid(self, form):
        old_order = Order.objects.get(pk=self.object.pk)
        response = super().form_valid(form)
        old_order.food.quantity += old_order.quantity
        old_order.food.save(update_fields=["quantity"])
        self.object.food.quantity -= self.object.quantity
        self.object.food.save(update_fields=["quantity"])
        messages.success(self.request, "Order updated successfully.")
        return response


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "orders/order_confirm_delete.html"
    success_url = reverse_lazy("orders:list")

    def form_valid(self, form):
        self.object.food.quantity += self.object.quantity
        self.object.food.save(update_fields=["quantity"])
        messages.success(self.request, "Order deleted and stock restored successfully.")
        return super().form_valid(form)
