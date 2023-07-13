from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home' ),
    path("weather",views.weatherPage,name='weatherPage' ),
    path("location",views.locationPage,name='locationPage' ),
]
