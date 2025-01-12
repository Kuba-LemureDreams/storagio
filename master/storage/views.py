from . import models, serializers
from rest_framework import generics, permissions
from . import permissions as my_perms


# Create your views here.
class ListCreateItems(generics.ListCreateAPIView):
    serializer_class = serializers.ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        name = self.request.query_params.get("name")

        if name:
            queryset = models.Item.objects.filter(name=name)
        else:
            queryset = models.Item.objects.all()

        return queryset


class RetrieveUpdateDeleteItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListCreatePlace(generics.ListCreateAPIView):
    serializer_class = serializers.PlaceSerializer
    queryset = models.Place.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateDeletePlace(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListCreateItemPlaced(generics.ListCreateAPIView):
    serializer_class = serializers.ItemPlacedSerializer
    queryset = models.ItemPlaced.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateDeletePlacement(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ItemPlacedSerializer
    queryset = models.ItemPlaced.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ListCreateUserPlacement(generics.ListCreateAPIView):
    serializer_class = serializers.UserPlacementSerializer
    queryset = models.UserPlacement.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveUpdateDeleteUserPlacement(generics.ListCreateAPIView):
    serializer_class = serializers.UserPlacementSerializer
    queryset = models.UserPlacement.objects.all()
    permission_classes = [my_perms.IsCreator]


class ListUser(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = [permissions.IsAdminUser]


class RegisterUser(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = [my_perms.IsNotAuthenticated]
