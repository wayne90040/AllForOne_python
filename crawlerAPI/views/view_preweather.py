from django.http import JsonResponse
import json, requests

url = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=rdec-key-123-45678-011121314&format=JSON"
re = requests.get(url, verify=False)
js = json.loads(re.content)
preweather_datas = js['cwbopendata']["dataset"]["location"]


def formatCityName(cityName):
    result = ""
    if cityName == "Taipei":
        result = "臺北市"

    return result


def post(request):
    result = {'result': 0}
    body = json.loads(request.body.decode(encoding='utf-8'))
    body_city = body['City']

    try:
        for preweather_data in preweather_datas:
            if preweather_data['locationName'] == formatCityName(body_city):
                result['locationName'] = preweather_data['locationName']
                result['weatherElement'] = preweather_data['weatherElement']

    except Exception as e:
        result['Exception'] = str(e)

    return JsonResponse(result)
