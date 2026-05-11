from django.db import models

from common.models import CommonModel


class Anime(CommonModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.title
