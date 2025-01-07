from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models
from .middleware import get_current_user


@receiver(post_save, sender=models.ItemPlaced)
def create_link_for_new_placement(sender, instance, created, **kwargs):
    if created:
        user = get_current_user()
        models.UserPlacement.objects.create(
            placement=instance,
            quantity=instance.no_in_packs * instance.quantity_of_packs,
            user=user,
        )
