from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Viewer(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    image = models.OneToOneField("core.ProfileImage", on_delete=models.CASCADE, related_name='profile_image', null=True, blank=True)
    watchlist = models.ManyToManyField("series.WebSeries", related_name='watched', blank=True)
    favorites = models.ManyToManyField("series.WebSeries", related_name='favorites', blank=True)
    completed = models.ManyToManyField("series.WebSeries", related_name='completed', blank=True)

    def __str__(self) -> str:
        return self.user.username

@receiver(post_save, sender=User)
def create_viewer(sender, instance, created, **kwargs):
    if created:
        Viewer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_viewer(sender, instance, **kwargs):
    instance.viewer.save()