from django.contrib import admin

from .models import Anime, Episode, Series


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):

    list_display = ("title",)


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):

    list_display = (
        "series",
        "title",
        "release_date",
        "genres",
        "tags",
        "type",
        "age_rating",
        "is_complete",
    )


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):

    list_display = ("anime", "title", "episode_number", "release_date", "duration")
