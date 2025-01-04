from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from . import models, serializers
from rest_framework import generics, status

# Create your views here.
class ListCreateItems(generics.ListCreateAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

class ListCreatePlace(generics.ListCreateAPIView):
    serializer_class = serializers.PlaceSerializer
    queryset = models.Place.objects.all()

class ListCreateItemPlaced(generics.ListCreateAPIView):
    serializer_class = serializers.ItemPlacedSerializer
    queryset = models.ItemPlaced.objects.all()

class ListCreateUserPlacement(generics.ListCreateAPIView):
    serializer_class = serializers.UserPlacementSerializer
    queryset = models.UserPlacement.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListUser(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class RegisterUser(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()