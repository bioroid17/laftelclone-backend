from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class UserDetail(APIView):
    def get(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
