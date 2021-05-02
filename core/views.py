from django.shortcuts import render
from series.views import WebSeries

# Create your views here.
def index(request):
    series = WebSeries.objects.all()
    return render(request, 'index.html', {'series':series})