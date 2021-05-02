from django.db import models
from datetime import timedelta
from django.urls import reverse


# Create your models here.
class WebSeries(models.Model):
    class Meta:
        verbose_name_plural = 'WebSeries'

    title = models.CharField(max_length=100)
    visit_url = models.URLField(max_length=200, default="https://youtube.com/")
    cover_image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    carousel_images = models.ManyToManyField("core.SeriesImage", related_name='carousel_images', blank=True)
    no_of_episodes = models.IntegerField(default=1)
    episode_watchtime =  models.DurationField(default=timedelta(hours=1, minutes=0, seconds=0))
    genre = models.CharField(max_length=50)
    platform_name = models.CharField(max_length=50, default="YouTube", blank=True)
    platform_url = models.URLField(max_length=200, default="https://youtube.com/", blank=True)
    description = models.TextField(default="", blank=True)
    tags = models.ManyToManyField('series.Tag', related_name='series')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('series:series', args=[str(self.id)])


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def clean(self) -> None:
        self.name = self.name.lower()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('series:tag_series', args=[str(self.name)])