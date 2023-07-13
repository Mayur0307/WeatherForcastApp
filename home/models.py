from django.db import models

class WeatherData(models.Model):
    latitude = models.DecimalField(max_digits=20, decimal_places=16)
    longitude = models.DecimalField(max_digits=20, decimal_places=16)
    temperature = models.FloatField(null=True)
    feels_like = models.FloatField(null=True)
    temp_min = models.FloatField(null=True)
    temp_max = models.FloatField(null=True)
    pressure = models.IntegerField(null=True)
    humidity = models.IntegerField(null=True)
    wind_speed = models.FloatField(null=True)
    wind_deg = models.IntegerField(null=True)
    clouds_all = models.IntegerField(null=True,default=None)
    updated_at = models.DateTimeField(auto_now=True)
    city=models.TextField(null=True)
    country=models.TextField(null=True)
