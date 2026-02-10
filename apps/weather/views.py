# views.py
from django.shortcuts import render
from .forecast import get_weather_for_cities

def weather_page(request):
    weather_data = get_weather_for_cities()

    return render(request, "page/weather.html", {
        "weather": weather_data
    })
