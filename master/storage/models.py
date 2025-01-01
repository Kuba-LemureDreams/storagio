from django.db import models
from django.contrib.auth.models import AbstractUser

#Models below
class Place(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ItemPlaced(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    no_in_packs = models.PositiveSmallIntegerField(default = 1)
    quantity_of_packs = models.PositiveSmallIntegerField(default = 1)
    placed_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    REQUIRED_FIELDS = ["first_name"]

class UserPlacement(models.Model):
    Roles = [
        (0, "Owner"),
        (1, "Viewer"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    placement = models.ForeignKey(ItemPlaced, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default = 1)
    role = models.CharField(max_length=50, default = 0, choices=Roles)
    assigned_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
