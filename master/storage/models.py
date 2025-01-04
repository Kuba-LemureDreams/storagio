from django.db import models
from django.contrib.auth.models import AbstractUser

#Models below
class Place(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ItemPlaced(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    no_in_packs = models.PositiveSmallIntegerField(default = 1, null = False, blank = False)
    quantity_of_packs = models.PositiveSmallIntegerField(default = 1, null = False, blank = False)
    placed_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity_of_packs * self.no_in_packs} of {self.item} in {self.place}"

class User(AbstractUser):
    REQUIRED_FIELDS = ["first_name"]

class UserPlacement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    placement = models.ForeignKey(ItemPlaced, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default = 1)
    assigned_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
