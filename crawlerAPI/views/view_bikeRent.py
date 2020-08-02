from django.http import JsonResponse
from datetime import datetime, timedelta
from wsgiref.handlers import format_date_time
from math import radians, cos, sin, asin, sqrt
from time import mktime
from hashlib import sha1
import json, requests
import hmac
import base64

app_id = 'ea0b964c043b4c19a7e8cb52511842be'
app_key = '3MjiMorUMhlsPR0SbjDCRGS06_s'


class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }


class Bike():
    def __init__(self, city):
        self.city = city

    def get_bike(self):
        auth = Auth(app_id, app_key)

        id_urls = {"Taipei": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/Taipei?$format=JSON",
                   "NewTaipei": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/NewTaipei?$format=JSON",
                   "Hsinchu": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/Hsinchu?$format=JSON",
                   "MiaoliCounty": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/MiaoliCounty?$format=JSON",
                   "ChanghuaCounty": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/ChanghuaCounty?$format=JSON",
                   "PingtungCounty": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/PingtungCounty?$format=JSON",
                   "Taoyuan": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/Taoyuan?$format=JSON",
                   "Kaohsiung": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/Kaohsiung?$format=JSON",
                   "Tainan": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/Tainan?$format=JSON",
                   "Taichung": "https://ptx.transportdata.tw/MOTC/v2/Bike/Station/Taichung?$format=JSON"}
        bike_urls = {"Taipei": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/Taipei?$format=JSON",
                     "NewTaipei": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/NewTaipei?$format=JSON",
                     "Hsinchu": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/Hsinchu?$format=JSON",
                     "MiaoliCounty": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/MiaoliCounty?$format=JSON",
                     "ChanghuaCounty": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/ChanghuaCounty?$format=JSON",
                     "PingtungCounty": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/PingtungCounty?$format=JSON",
                     "Taoyuan": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/Taoyuan?$format=JSON",
                     "Kaohsiung": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/Kaohsiung?$format=JSON",
                     "Tainan": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/Tainan?$format=JSON",
                     "Taichung": "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/Taichung?$format=JSON"}
        id_url = id_urls[self.city]
        bike_url = bike_urls[self.city]

        id_re = requests.get(id_url, headers=auth.get_auth_header(), verify=False)
        bike_re = requests.get(bike_url, headers=auth.get_auth_header(), verify=False)
        id_js = json.loads(id_re.content)
        bike_js = json.loads(bike_re.content)
        bike_list = []

        for id_ in id_js:
            for bike in bike_js:
                if id_['StationUID'] == bike['StationUID']:
                    stationUID = id_['StationUID']
                    stationID = id_['StationID']
                    stationName_zh = id_['StationName']['Zh_tw']
                    # stationName_en = id_['StationName']['En']
                    stationLatitude = id_['StationPosition']['PositionLat']
                    stationLongitude = id_['StationPosition']['PositionLon']
                    stationAddress_zh = id_['StationAddress']['Zh_tw']
                    # stationAddress_en = a['StationAddress']['En']
                    bikesCapacity = id_['BikesCapacity']
                    servieAvailable = bike['ServiceAvailable']  # 服務狀態:[0:'停止營運',1:'正常營運']
                    availableRentBikes = bike['AvailableRentBikes']  # 可租借個數
                    availableReturnBikes = bike['AvailableReturnBikes']  # 可歸還數
                    updateTime = id_['UpdateTime']

            bikedic = {'StationUID': stationUID, 'StationID': stationID, 'StationName_zh': stationName_zh,
                       'StationLatitude': stationLatitude,
                       'StationLongitude': stationLongitude, 'stationAddress_zh': stationAddress_zh,
                       'BikesCapacity': bikesCapacity,
                       'ServiceAvailable': servieAvailable, 'AvailableRentBikes': availableRentBikes,
                       'AvailableReturnBikes': availableReturnBikes,
                       'UpdateTime': updateTime}

            bike_list.append(bikedic)

        return bike_list


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    d_lon = lon2 - lon1  # haversine公式
    d_lat = lat2 - lat1
    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


def get_all_bike(request):
    result = {'result': 0}
    body = json.loads(request.body.decode(encoding="utf-8"))
    body_city = body['City']

    try:
        city_bikes = Bike(body_city).get_bike()
    except Exception as e:
        result['Exception'] = str(e)

    if len(city_bikes) == 0:
        result['type'] = '全部站點'
        result['bikes'] = {'error': '連線異常，請稍後再試'}
    else:
        result['result'] = 1
        result['type'] = '全部站點'
        result['bikes'] = city_bikes

    return JsonResponse(result)


def get_close_bike(request):
    result = {'result': 0}
    body = json.loads(request.body.decode(encoding="utf-8"))

    body_lon = body["Longitude"]
    body_lat = body["Latitude"]
    body_city = body["City"]
    body_type = body["Type"]
    haver_list = []

    city_bikes = Bike(body_city).get_bike()

    # Get Min haversine
    for city_bike in city_bikes:
        haver = haversine(body_lon, body_lat, float(city_bike['StationLongitude']), float(city_bike['StationLatitude']))
        haver_list.append(haver)
    haver_min = min(haver_list)

    for city_bike in city_bikes:
        if body_type == 1:
            try:
                if haver_min == haversine(body_lon, body_lat, float(city_bike['StationLongitude']), float(city_bike['StationLatitude'])):
                    result['result'] = 1
                    result['type'] = "自己最近站點"
                    city_bike['haversine'] = str(haver_min).split(".")[0]
                    result['bikes'] = [city_bike]
                    break
            except Exception as e:
                result['Exception'] = str(e)

    if result['result'] == 0:
        result['error'] = '主機異常，請稍後再試'

    return JsonResponse(result)








