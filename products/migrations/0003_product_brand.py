# Generated by Django 5.1.2 on 2024-10-31 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_product_image1_product_image2_product_image3"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
