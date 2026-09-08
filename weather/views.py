from django.shortcuts import render
import requests



def show_temp_view(request):

    lat, lon = 37.7981, 48.5146
    url = f"https://api.open-meteo.com/v1/forcast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        data = requests.get(url).json()
        temp = data['current_weather']['temperature']
    except Exception:
        temp = None


    context = {
        'city': 'Hamedan',
        'temp': temp,
    }

    return render(request, 'show_temp.html', context)
