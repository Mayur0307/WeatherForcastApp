from django.db import models

class WeatherData(models.Model):
    latitude = models.DecimalField(max_digits=20, decimal_places=16)
    longitude = models.DecimalField(max_digits=20, decimal_places=16)
    temperature = models.FloatField(null=True)
    feelslike = models.FloatField(null=True)
    tempmin = models.FloatField(null=True)
    tempmax = models.FloatField(null=True)
    pressure = models.IntegerField(null=True)
    humidity = models.IntegerField(null=True)
    windspeed = models.FloatField(null=True)
    winddeg = models.IntegerField(null=True)
    cloudsall = models.IntegerField(null=True,default=None)
    updatedat = models.DateTimeField(auto_now=True)
    city=models.TextField(null=True)
    country=models.TextField(null=True)
