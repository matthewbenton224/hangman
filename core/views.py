from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from core.models import User, Chryon
from core.serializers import ChryonSerializer, UserSerializer
from rest_framework.views import APIView

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class ChryonListCreateView(ListCreateAPIView):
    queryset = Chryon.objects.all()
    serializer_class = ChryonSerializer
    # permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request):
        chryons = Chryon.objects.all()
        serializer = ChryonSerializer(
            chryons, many=True)
        return Response(serializer.data)


