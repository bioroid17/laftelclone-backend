from .models import Anime
from .serializers import AnimeSerializer, SeriesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Animes(APIView):
    def get(self, request):
        animes = Anime.objects.all()
        serializer = AnimeSerializer(animes, many=True)
        return Response(serializer.data)


class AnimeDetail(APIView):
    def get(self, request, anime_pk):
        anime = Anime.objects.get(pk=anime_pk)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)


class AnimeSeries(APIView):
    def get(self, request, anime_pk):
        anime = Anime.objects.get(pk=anime_pk)
        series = anime.series
        serializer = SeriesSerializer(series)
        return Response(serializer.data)
