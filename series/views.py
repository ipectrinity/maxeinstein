from django.shortcuts import render
from .models import WebSeries, Tag
from django.shortcuts import get_object_or_404


def series_index(request):
    series = WebSeries.objects.all()
    return render(request, 'series/index.html', {'series':series})

def series(request, id):
    series = get_object_or_404(WebSeries, pk=id)
    return render(request, 'series/series.html', {'object': series})

def tag_series(request, name):
    name = name.lower()
    title = 'Series about {}'.format(name)
    tag = get_object_or_404(Tag, name=name)
    series = WebSeries.objects.filter(tags=tag)
    return render(request, 'series/filtered_series_list.html',
                  {'series':series, 'title':title})

def genre_series(request, name):
    name = name.lower()
    title = name.upper()
    series = WebSeries.objects.filter(genre__contains=name)
    return render(request, 'series/filtered_series_list.html',
                  {'series':series, 'title':title})