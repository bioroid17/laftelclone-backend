from .models import Anime
from .serializers import AnimeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Animes(APIView):
    def get(self, request):
        animes = Anime.objects.all()
        serializer = AnimeSerializer(animes, many=True)
        return Response(serializer.data)
