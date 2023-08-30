from django.shortcuts import render, reverse, redirect
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.http import HttpResponse
from .models import Advertisements
from .Forms import AdvertisementForm


def advertisement_view(request, pk):
    advertisements = Advertisements.objects.get(pk=pk)
    context = {
        'advertisements': advertisements
    }
    return render(request, 'app_djangosite/advertisement.html', context=context)

def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisements.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'app_djangosite/index.html', context=context)

def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count('advertisements')
    ).order_by('-adv_count')
    context = {'users': users}
    return render(request, 'app_djangosite/top-sellers.html', context=context)

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