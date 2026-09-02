from django.shortcuts import render
from django.http import HttpResponse


def show_temp_view(request):
    return HttpResponse("hello there")
