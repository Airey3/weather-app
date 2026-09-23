from django.urls import path
from .views import show_temp_view


urlpatterns = [
    path("", show_temp_view, name='home'),
]



