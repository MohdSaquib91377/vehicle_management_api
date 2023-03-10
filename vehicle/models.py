from django.db import models
from account import models as account_models
# Create your models here.

class Vehicle(account_models.TimeStampedModel):
    VEHICLE_TYPE_CHOICES = (
        ("Two","Two"),
        ("Three","Three"),
        ("Four Wheelers","Four Wheelers")
    )
    number = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=16, choices=VEHICLE_TYPE_CHOICES)

    class Meta:
        ordering = ("-created_at",)
    