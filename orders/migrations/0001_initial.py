# Generated manually for the beginner-friendly Food Management System.
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("foods", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("customer_name", models.CharField(max_length=150)),
                ("customer_phone", models.CharField(max_length=20)),
                ("quantity", models.PositiveIntegerField()),
                ("total_price", models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="foods.food",
                    ),
                ),
            ],
            options={
                "ordering": ["-order_date"],
            },
        ),
    ]
