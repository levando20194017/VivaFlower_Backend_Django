# Generated by Django 4.2.15 on 2024-10-24 16:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("product", "0001_initial"),
        ("order_detail", "0001_initial"),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductSale",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("sale_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity_sold", models.IntegerField()),
                (
                    "vat",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "shipping_cost",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("sale_date", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "delete_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "order_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="order_detail.orderdetail",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.store"
                    ),
                ),
            ],
        ),
    ]
