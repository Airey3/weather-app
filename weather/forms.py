from django import forms 
from .models import City, Products


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["lat", "lon", "title"]


class productsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price']




        