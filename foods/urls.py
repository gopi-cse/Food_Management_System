from django.urls import path

from .views import FoodCreateView, FoodDeleteView, FoodListView, FoodUpdateView

app_name = "foods"

urlpatterns = [
    path("", FoodListView.as_view(), name="list"),
    path("create/", FoodCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", FoodUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", FoodDeleteView.as_view(), name="delete"),
]
