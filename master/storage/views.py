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

class ListUser(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

    #def get_queryset(self):
        #return models.User.objects.filter(username=self.request.user)

class RegisterUser(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class LoginView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)