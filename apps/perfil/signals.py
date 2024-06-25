from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from perfil.models import Perfil


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_perfil(sender, **kwargs):
    if kwargs.get('created', False):
        Perfil.objects.create(usuario=kwargs['instance'])
