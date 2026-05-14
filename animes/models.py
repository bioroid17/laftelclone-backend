from django.db import models

from common.models import CommonModel


class Series(CommonModel):

    class Meta:
        verbose_name_plural = "Series"

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Anime(CommonModel):

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
    genres = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Comma-separated genres (e.g., SF, 모험, 개그)",
    )
    tags = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Comma-separated tags (e.g., 가족, 로봇, 게임)",
    )
    type = models.CharField(
        max_length=15,
        choices=TypeChoices.choices,
        default=TypeChoices.TVA,
    )
    age_rating = models.PositiveSmallIntegerField(
        choices=AgeRatingChoices.choices,
        default=AgeRatingChoices.ALL,
    )
    is_available = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)
    is_only_on_laftel = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Episode(CommonModel):

    anime = models.ForeignKey(
        to=Anime,
        on_delete=models.CASCADE,
        related_name="episodes",
    )
    title = models.CharField(max_length=255)
    episode_number = models.PositiveIntegerField()
    release_date = models.DateField()
    """
    DurationField는 내부적으로 시간 간격을 초 단위로 저장하지만, 입력과 출력 시에는 "HH:MM:SS" 형식으로 처리됩니다. 이를 통해 에피소드의 재생 시간을 직관적으로 관리할 수 있습니다. Python에서는 datetime.timedelta 객체로 DurationField 값을 다룰 수 있습니다.
    """
    duration = models.DurationField(default="00:00:00")

    def __str__(self):
        return f"{self.anime.title} - {self.episode_number}화: {self.title}"
