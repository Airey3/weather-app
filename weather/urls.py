from django.urls import path
from .views import show_temp_view, city_list_view


urlpatterns = [
    path("", show_temp_view, name='home'),
    path("city-list", city_list_view, name='city_list'),
]



