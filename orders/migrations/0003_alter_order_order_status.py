# Generated by Django 5.1.2 on 2024-11-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_alter_ordereditem_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.IntegerField(
                choices=[
                    (1, "Order Confirmed"),
                    (2, "Order Processed"),
                    (3, "Order Delivered"),
                    (4, "Order Rejected"),
                ],
                default=0,
            ),
        ),
    ]