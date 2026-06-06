from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from categories.models import Category
from .forms import FoodForm
from .models import Food


class FoodListView(LoginRequiredMixin, ListView):
    model = Food
    template_name = "foods/food_list.html"
    context_object_name = "foods"
    paginate_by = 6

    def get_queryset(self):
        queryset = Food.objects.select_related("category")
        query = self.request.GET.get("q", "").strip()
        category_id = self.request.GET.get("category", "").strip()
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(category__name__icontains=query)
            )
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.order_by("name")
        context["search_query"] = self.request.GET.get("q", "")
        context["selected_category"] = self.request.GET.get("category", "")
        return context


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    form_class = FoodForm
    template_name = "foods/food_form.html"
    success_url = reverse_lazy("foods:list")

    def form_valid(self, form):
        messages.success(self.request, "Food item created successfully.")
        return super().form_valid(form)


class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    form_class = FoodForm
    template_name = "foods/food_form.html"
    success_url = reverse_lazy("foods:list")

    def form_valid(self, form):
        messages.success(self.request, "Food item updated successfully.")
        return super().form_valid(form)


class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = "foods/food_confirm_delete.html"
    success_url = reverse_lazy("foods:list")

    def form_valid(self, form):
        messages.success(self.request, "Food item deleted successfully.")
        return super().form_valid(form)
