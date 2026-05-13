from rest_framework.serializers import ModelSerializer
from .models import Anime, Series


class SeriesSerializer(ModelSerializer):
    class Meta:
        model = Series
        exclude = ("created_at", "updated_at")


class AnimeSerializer(ModelSerializer):

    series = SeriesSerializer()

    class Meta:
        model = Anime
        fields = "__all__"
