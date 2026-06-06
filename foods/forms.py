from django import forms

from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["name", "category", "price", "quantity", "description", "expiry_date", "image"]
        widgets = {
            "expiry_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }
