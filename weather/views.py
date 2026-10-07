from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
import requests


def add_city_view(request):
     
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect("city_list")
    else:
        form = CityForm()

    context = {'form': form}
    
    return render(request, "add_city.html", context)


def show_temp_view(request):

    city_id = request.GET.get('id')

    if city_id:
        city = City.objects.get(id=city_id)
    else:
            city = City.objects.first()


    lat, lon = city.lat, city.lon
    url = f"https://api.open-meteo.com/v1/forcast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        data = requests.get(url).json()
        temp = data['current_weather']['temperature']
    except Exception:
        temp = None

    context = {
        'city': city.title,
        'temp': temp,
    }

    return render(request, 'show_temp.html', context)


def city_list_view(request):
    cities = City.objects.all()
    context = {"cities": cities}
    return render(request, "city_list.html", context)


def delete_city_view(request):
    if request.method == "POST":
        city_id = request.POST.get('id')
        city = City.objects.filter(id=city_id) 

        if city:
            city.delete()

    return redirect('city_list')


