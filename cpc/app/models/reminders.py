from django.db import models
from django_extensions.db.models import TimeStampedModel


class ProductReminder(TimeStampedModel):
    shopify_id = models.BigIntegerField(
        blank=True,
        null=True,
        help_text="If present search is done by shopify_id else by title",
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    threshold = models.IntegerField(
        default=0,
        help_text="Threshold for the product, if below a reminder will be sent.",
    )

    def __str__(self):
        return f"{self.title if self.title else 'Unknown Name'} - {self.shopify_id}"
