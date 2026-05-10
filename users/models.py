from django.db import models
from django.contrib.auth.models import AbstractUser

from common.models import CommonModel


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

    def __str__(self):
        return self.username


class Profile(CommonModel):

    class AgeRatingChoices(models.IntegerChoices):
        ALL = (0, "ALL")
        R7 = (7, "7세")
        R12 = (12, "12세")
        R15 = (15, "15세")
        R19 = (19, "19세")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    name = models.CharField(
        max_length=15,
    )
    age_rating = models.PositiveSmallIntegerField(
        choices=AgeRatingChoices.choices,
        default=AgeRatingChoices.ALL,
    )

    def __str__(self):
        return f"{self.user.username}'s Profile: {self.name}"
