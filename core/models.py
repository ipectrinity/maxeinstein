from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class SeriesImage(models.Model):
    series_name = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)
    
    def __str__(self) -> str:
        return f'{self.series_name}_series_image'


class ProfileImage(models.Model):
    username = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.username}_profile_image'


class Review(models.Model):
    user = models.OneToOneField("users.Viewer", on_delete=models.CASCADE)
    series = models.ManyToManyField("series.WebSeries", related_name='series')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    posted_on = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default="", blank=True)

    def __str__(self) -> str:
        return f'{self.series.title}_{self.user.name}_{self.posted_on}'