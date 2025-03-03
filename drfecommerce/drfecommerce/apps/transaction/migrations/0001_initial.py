# Generated by Django 4.2.15 on 2024-10-24 16:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("order_date", models.DateTimeField()),
                ("transaction_number", models.CharField(max_length=255)),
                ("amount", models.FloatField()),
                ("bank_code", models.CharField(max_length=50)),
                ("bank_status", models.CharField(max_length=50)),
                ("bank_message", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="order.order",
                    ),
                ),
            ],
        ),
    ]
