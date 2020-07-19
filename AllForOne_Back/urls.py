"""AllForOne_Back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crawlerAPI.views import view_airQuality, view_warning, view_gasPrice, view_bikeRent, view_weather, view_preweather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AQI/', view_airQuality.post),
    path('WARN/', view_warning.post),
    path('GasPrice/', view_gasPrice.post),
    path('Bike/', view_bikeRent.get_all_bike),
    path('CloseBike/', view_bikeRent.get_close_bike),
    path('Weather/', view_weather.post),
    path('PreWeather/', view_preweather.post)
]
