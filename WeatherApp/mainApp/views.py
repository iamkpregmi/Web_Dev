from urllib.error import URLError
from django.shortcuts import render
from django.contrib import messages
import urllib.request
import json

# def home(request):
#     if request.method == 'POST':
#         city = request.POST.get("cityname")
#         source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&'+"&appid=f22f1cafaa4e1e9f0e768a3a7011348d").read()
#         list_of_data = json.loads(source)
#         data = {
#         "country_code": str(list_of_data['sys']['country']),
#         "temp": str(round(int(list_of_data['main']['temp'])-273.15,2)),
#         "city": city
#         }
#     else:
#         data = {}    
#     return render(request,"index.html",data)

def home(request):
    if request.method == 'POST':
        data = None
        try:
            city = request.POST.get("cityname")
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&'+"&appid=f22f1cafaa4e1e9f0e768a3a7011348d").read()
            list_of_data = json.loads(source)
            data = {
            "country_code": str(list_of_data['sys']['country']),
            "weather": str(list_of_data['weather'][0]['main']),
            "temp": str(round(int(list_of_data['main']['temp'])-273.15,2)),
            "temp_min": str(round(int(list_of_data['main']['temp_min'])-273.15,2)),
            "temp_max": str(round(int(list_of_data['main']['temp_max'])-273.15,2)),
            "city": city
            }
        except:
            messages.error(request,"City Not Found")
    else:
        data = {}    
    return render(request,"index.html",data)