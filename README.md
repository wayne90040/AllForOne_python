## AllForOne_Django
#### Heroku-Django Practice

<details>
  <summary> 簡介 </summary>
   
   - AllForOne API backstage
   
   - 開發工具
      - Pycharm
      - Django 3.0.8
    
   - Note
      - How to use Heroku
      
      - How to use AllForOne API
</details>


## How to use Heroku

### Create requirements.txt 
> pip freeze > requirements.txt

### Create Procfile

#### Web: 
> gunicorn --pythonpath siteName siteName.wsgi 

#### xxx.py: 
> xxx: python xxx.py

### Create production_settings.py for Heroku
* Path: 
> siteName/siteName/production_settings.py 

* Code:

```python
# Import all default settings.
from .settings import *

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}

# Static asset configuration.
STATIC_ROOT = 'staticfiles'

# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers.
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode.
DEBUG = False
```
### wsgi.py
* Path: 
> siteName/siteName/wsgi.py

```python
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siteName.settings")
application = Cling(get_wsgi_application())
```

## How to use AllForOne API

> https://allforone-back.herokuapp.com/

Url | Memo |
|:---:|:---:|
|AQI/ | 空氣品質 | 
|WARN/ | 警報 | 
|GasPrice/ | 油價 | 
|Bike/ | Ubike |
|CloseBike/| 最近Bike |
|Weather/ | 氣溫 |
|PreWeather/ | 近36小時氣溫 |

<details>
<summary> AQI/(空氣品質) </summary>

* request:
```json
{
    "Longitude": 120.000, 
    "Latitude": 20.000
}
```
* response: 
```json
{
    "result": 1,
    "SiteName": "",
    "County": "",
    "AQI": "",
    "Pollutant": "",
    "AQIStatus": "",
    "PM10": "",
    "PM25": "",
    "WindSpeed": "",
    "WindDir": "",
    "PM10Avg": "",
    "PM25Avg": "",
    "Date": "",
    "Time": "",
    "So2": "",
    "Co": "",
    "O3": "",
    "So2Avg": "",
    "PM25Status": ""
}
```
</details>

<details>
<summary> WARN/(警報) </summary>
  
* request:
```json
{
    "City": "高雄市"
}
```

* response: 
```json
{
    "result": 1,
    "locationName": "",
    "hazardConditions": ""
}
```
</details>

<details>
<summary> GasPrice/(油價) </summary>
  
* request:
  * "All" - 回傳全部
```json
{
    "Type": "Unleaded" 
}
```

* response: 
```json
{
    "result": 1,
    "Unleaded": 22.4
}
```
</details>

<details>
<summary> Bike/(All Ubike) </summary>
 
* request:
```json
{
    "City": "Taipei"
}
```

* response: 
```json
{
    "result": 1,
    "type": "全部站點",
    "bikes": [
        {
            "StationUID": "",
            "StationID": "",
            "StationName_zh": "",
            "StationLatitude": 24.97848,
            "StationLongitude": 121.55545,
            "stationAddress_zh": "",
            "BikesCapacity": 26,
            "ServiceAvailable": 1,
            "AvailableRentBikes": 15,
            "AvailableReturnBikes": 11,
            "UpdateTime": "",
            "haversine": ""
        }
    ]
}
```
</details>

<details>
<summary> CloseBike/(最近Bike) </summary>

* request:
```json
{
    "Longitude": 120.000, 
    "Latitude": 20.000,
    "City": "Taipei",
    "Type": 1
}
```
* response: 
```json
{
    "result": 1,
    "type": "自己最近站點",
    "bikes": [
        {
            "StationUID": "",
            "StationID": "",
            "StationName_zh": "",
            "StationLatitude": 24.97848,
            "StationLongitude": 121.55545,
            "stationAddress_zh": "",
            "BikesCapacity": 26,
            "ServiceAvailable": 1,
            "AvailableRentBikes": 15,
            "AvailableReturnBikes": 11,
            "UpdateTime": "",
            "haversine": ""
        }
    ]
}
```

</details>
  
<details>
<summary> Weather/(氣溫) </summary>
  
* request:
```json
{
    "Longitude": 120.000, 
    "Latitude": 20.000
}
```
* response: 
```json
{
    "result": 1,
    "locationName": "恆春",
    "WDIR": "130",
    "WDSD": "1.10",
    "TEMP": "26.40",
    "HUMD": "0.99",
    "RAINFALL": "0",
    "H_UVI": "0",
    "D_TX": "26.60",
    "D_TXT": "0020",
    "D_TN": "26.30",
    "D_TNT": "0008"
}
```

</details>

<details>
<summary> PreWeather/(近36小時氣溫) </summary>
  
* request:
```json
{
    "City": "Taipei"
}
```
* response: 
```json
{
    "result": 0,
    "locationName": "臺北市",
    "weatherElement": [
        {
            "elementName": "Wx",
            "time": [
                {
                    "startTime": "2020-08-16T00:00:00+08:00",
                    "endTime": "2020-08-16T06:00:00+08:00",
                    "parameter": {
                        "parameterName": "多雲",
                        "parameterValue": "4"
                    }
                },
                {
                    "startTime": "2020-08-16T06:00:00+08:00",
                    "endTime": "2020-08-16T18:00:00+08:00",
                    "parameter": {
                        "parameterName": "晴午後短暫雷陣雨",
                        "parameterValue": "21"
                    }
                },
                {
                    "startTime": "2020-08-16T18:00:00+08:00",
                    "endTime": "2020-08-17T06:00:00+08:00",
                    "parameter": {
                        "parameterName": "晴時多雲",
                        "parameterValue": "2"
                    }
                }
            ]
        }
    ]
}
```

</details>
  
  
  
