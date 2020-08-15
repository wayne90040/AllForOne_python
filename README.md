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

#### AQI/(空氣品質)
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
