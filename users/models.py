from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class MembershipChoices(models.TextChoices):
        BASIC = ("basic", "Basic")
        PREMIUM = ("premium", "Premium")

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    membership = models.CharField(
        max_length=7,
        choices=MembershipChoices.choices,
        null=True,
        blank=True,
        help_text="User membership type (basic or premium)",
    )
