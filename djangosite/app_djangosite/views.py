from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Advertisements
from .Forms import AdvertisementForm

def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_djangosite/index.html', context=context)

def top_sellers(request):
    return render(request, 'app_djangosite/top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            return redirect('main-page')
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_djangosite/advertisement-post.html', context=context)