# Generated by Django 4.2.9 on 2024-02-03 05:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productreminder",
            name="shopify_id",
            field=models.BigIntegerField(
                blank=True,
                help_text="If present search is done by shopify_id else by title",
                null=True,
            ),
        ),
    ]
