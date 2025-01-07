from django.contrib.auth import authenticate
from . import models
from rest_framework import serializers


# serializers below
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = ["id", "name", "description"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ["id", "name", "description"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username", "first_name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return models.User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
        )


class ItemPlacedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemPlaced
        fields = [
            "item",
            "place",
            "quantity_of_packs",
            "no_in_packs",
            "placed_at",
            "last_modified",
        ]


class UserPlacementSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = models.UserPlacement
        fields = ["user", "placement", "quantity", "assigned_at", "last_modified"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user is None:
            raise serializers.ValidationError("Invalid input")
        if not user.is_active:
            raise serializers.ValidationError("User is disabled")
        data["user"] = user
        return data
