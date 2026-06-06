document.addEventListener("DOMContentLoaded", () => {
    const alerts = document.querySelectorAll(".alert-dismissible");
    alerts.forEach((alert) => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }, 4500);
    });

    const priceDataElement = document.getElementById("food-prices-data");
    const foodSelect = document.getElementById("id_food");
    const quantityInput = document.getElementById("id_quantity");
    const pricePreview = document.getElementById("pricePreview");

    if (priceDataElement && foodSelect && quantityInput && pricePreview) {
        const prices = JSON.parse(priceDataElement.textContent);

        const updatePreview = () => {
            const price = Number(prices[foodSelect.value] || 0);
            const quantity = Number(quantityInput.value || 0);
            if (price > 0 && quantity > 0) {
                pricePreview.textContent = `Estimated total: ₹${(price * quantity).toFixed(2)}`;
                pricePreview.classList.remove("alert-info");
                pricePreview.classList.add("alert-success");
            } else {
                pricePreview.textContent = "Choose a food item and quantity to preview the total.";
                pricePreview.classList.add("alert-info");
                pricePreview.classList.remove("alert-success");
            }
        };

        foodSelect.addEventListener("change", updatePreview);
        quantityInput.addEventListener("input", updatePreview);
        updatePreview();
    }
});
