from django.urls import path
from . import views

urlpatterns = [
    path("", views.Animes.as_view(), name="see_all_animes"),
]
