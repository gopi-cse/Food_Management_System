from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer_name", "customer_phone", "food", "quantity"]
        widgets = {
            "customer_phone": forms.TextInput(attrs={"placeholder": "Example: 9876543210"}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity

    def clean(self):
        """Prevent orders larger than available stock."""
        cleaned_data = super().clean()
        food = cleaned_data.get("food")
        quantity = cleaned_data.get("quantity")
        if food and quantity:
            available_quantity = food.quantity
            if self.instance.pk and self.instance.food_id == food.id:
                available_quantity += self.instance.quantity
            if quantity > available_quantity:
                raise forms.ValidationError(f"Only {available_quantity} units of {food.name} are available.")
        return cleaned_data
