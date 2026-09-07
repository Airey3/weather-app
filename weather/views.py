from django.shortcuts import render
from django.http import HttpResponse
import random   



def show_temp_view(request):
    temp = random.randint(-8, 20)
    context = {
        'city': 'Hamedan',
        'temp': temp,
    }

    return render(request, 'show_temp.html', context)
