from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from django.urls import reverse_lazy
from .forms import EmailUserCreationForm

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy(settings.LOGIN_REDIRECT_URL))
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = EmailUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
