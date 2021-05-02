from django.urls import path
from . import views

app_name = 'series'

urlpatterns = [
    path('tag/<str:name>', views.tag_posts, name='tag_series'),
    path('series/<int:id>', views.series, name='series'),
    path('', views.series_index, name='series_index'),
] 