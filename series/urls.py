from django.urls import path
from . import views

app_name = 'series'

urlpatterns = [
    path('genre/<str:name>', views.genre_series, name='genre_series'),
    path('tag/<str:name>', views.tag_series, name='tag_series'),
    path('series/<int:id>', views.series, name='series'),
    path('', views.series_index, name='series_index'),
] 