from django.db import models

from common.models import CommonModel


class Series(CommonModel):

    class Meta:
        verbose_name_plural = "Series"

    class AgeRatingChoices(models.IntegerChoices):
        ALL = (0, "ALL")
        R7 = (7, "7세")
        R12 = (12, "12세")
        R15 = (15, "15세")
        R19 = (19, "19세")

    class TypeChoices(models.TextChoices):
        TVA = ("tva", "TVA")
        MOVIE = ("movie", "극장판")
        OVA = ("ova", "OVA")
        ETC = ("etc", "기타")

    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    type = models.CharField(
        max_length=15,
        choices=TypeChoices.choices,
        default=TypeChoices.TVA,
    )
    age_rating = models.PositiveSmallIntegerField(
        choices=AgeRatingChoices.choices,
        default=AgeRatingChoices.ALL,
    )
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Anime(CommonModel):
    series = models.ForeignKey(
        to=Series,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="animes",
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title
