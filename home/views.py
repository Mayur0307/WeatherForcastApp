
from django.shortcuts import render
import requests
from django.utils import timezone


from home.models import WeatherData

def weatherPage(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        weatherType= request.POST.get('weatherType')
        api_key = '497e2198b9956d870fa2638f988b4d4a'

        # Check if weather data is already stored and within expiration time
        weather_data = WeatherData.objects.filter(latitude=latitude, longitude=longitude).first()
        if weather_data and (timezone.now() - weather_data.updated_at).total_seconds() <= 600:
            return render(request, 'weatherPage.html', {'weather_data': weather_data})
            # temperature = weather_data.temperature          
            # feels_like=weather_data.feels_like,
            # temp_min=weather_data.temp_min,
            # temp_max=weather_data.temp_max,
            # pressure=weather_data.pressure,
            # humidity=weather_data.humidity,
            # wind_speed=weather_data.wind_speed,
            # wind_deg=weather_data.wind_deg,
            # clouds_all=weather_data.clouds_all,
            # city=weather_data.city,
            # country=weather_data.country
            
        else:
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&exclude={weatherType}&appid={api_key}'
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
                weather_obj = WeatherData(
                    latitude=latitude,
                    longitude=longitude,
                    temperature=weather_data['main']['temp'],
                    feels_like=weather_data['main']['feels_like'],
                    temp_min=weather_data['main']['temp_min'],
                    temp_max=weather_data['main']['temp_max'],
                    pressure=weather_data['main']['pressure'],
                    humidity=weather_data['main']['humidity'],
                    wind_speed=weather_data['wind']['speed'],
                    wind_deg=weather_data['wind']['deg'],
                    clouds_all=weather_data['clouds']['all'],
                    city=weather_data['name'],
                    country=weather_data['sys']['country']
                )
                weather_obj.save()
                return render(request, 'weatherPage.html', {'weather_data': weather_obj})
            else:
                error_message = 'Failed to fetch weather data. Please try again.'
                return render(request, 'weatherPage.html', {'error_message': error_message})


    return render(request, 'weatherPage.html')

def index(request):
    return render(request,'index.html')

def locationPage(request):
    return render(request,'locationPage.html')
