# Generated by Django 4.2.2 on 2023-09-05 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("M", "Mobile"),
                    ("L", "Laptop"),
                    ("TW", "Top Wear"),
                    ("BW", "Bottom Wear"),
                    ("A", "Accessory"),
                ],
                max_length=2,
            ),
        ),
    ]