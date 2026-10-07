from django.urls import path
from .views import show_temp_view, city_list_view, add_city_view, delete_city_view


urlpatterns = [
    path("", show_temp_view, name='home'),
    path("city-list/", city_list_view, name='city_list'),
    path("add-city/", add_city_view, name='add_city'),
    path("delete-city/", delete_city_view, name='delete_city'),
]



