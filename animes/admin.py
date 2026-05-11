from django.contrib import admin

from .models import Anime, Series


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "release_date",
    )


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "genre",
        "type",
        "age_rating",
        "is_complete",
    )
