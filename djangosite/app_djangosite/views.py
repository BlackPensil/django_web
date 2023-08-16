from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Advertisements
from .Forms import AdvertisementForm

def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context=context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context=context)