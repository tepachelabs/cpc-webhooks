# Generated by Django 4.2.9 on 2024-02-03 05:12

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app", "0002_delete_reminder"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductReminder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("shopify_id", models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
    ]