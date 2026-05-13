from django.urls import path
from . import views

urlpatterns = [
    path("", views.Animes.as_view(), name="all_animes"),
    path("<int:anime_pk>/", views.AnimeDetail.as_view(), name="anime_detail"),
    path("<int:anime_pk>/series", views.AnimeSeries.as_view(), name="anime_series"),
]
