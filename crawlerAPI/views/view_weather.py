from django.http import JsonResponse
import json, requests

url = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0003-001?Authorization=rdec-key-123-45678-011121314&format=JSON"
re = requests.get(url, verify=False)
js = json.loads(re.content)
weather_datas = js['cwbopendata']['location']


def post(request):
    result = {'result': 0}
    body = json.loads(request.body.decode(encoding='utf-8'))
    body_lon = body['Longitude']
    body_lat = body['Latitude']
    hypotenuse_list = []

    try:
        for weather_data in weather_datas:
            hypotenuse = (float(weather_data['lon']) - float(body_lon)) ** 2 + (float(weather_data['lat']) - float(body_lat)) ** 2
            hypotenuse_list.append(hypotenuse)
        min_hpy = min(hypotenuse_list)

        for weather_data in weather_datas:
            if min_hpy == (float(weather_data['lon']) - float(body_lon)) ** 2 + (float(weather_data['lat']) - float(body_lat)) ** 2:
                result['result'] = 1
                result['locationName'] = weather_data['locationName']

                weatherElements = weather_data['weatherElement']
                for weatherElement in weatherElements:
                    # 風向
                    if weatherElement["elementName"] == "WDIR":
                        result['WDIR'] = weatherElement['elementValue']['value']
                    # 風速
                    elif weatherElement["elementName"] == "WDSD":
                        result['WDSD'] = weatherElement['elementValue']['value']
                    # 溫度
                    elif weatherElement["elementName"] == "TEMP":
                        result['TEMP'] = weatherElement['elementValue']['value']
                    # 濕度
                    elif weatherElement["elementName"] == "HUMD":
                        result['HUMD'] = weatherElement['elementValue']['value']
                    # 24 小時降雨量
                    elif weatherElement["elementName"] == "24R":
                        result['RAINFALL'] = weatherElement['elementValue']['value']
                    # 每小時紫外線
                    elif weatherElement["elementName"] == "H_UVI":
                        result['H_UVI'] = weatherElement['elementValue']['value']
                    # 最高溫度
                    elif weatherElement["elementName"] == "D_TX":
                        result['D_TX'] = weatherElement['elementValue']['value']
                    # 最高溫度發生時間
                    elif weatherElement["elementName"] == "D_TXT":
                        result['D_TXT'] = weatherElement['elementValue']['value']
                    # 最低溫度
                    elif weatherElement["elementName"] == "D_TN":
                        result['D_TN'] = weatherElement['elementValue']['value']
                    # 最低溫度發生時間
                    elif weatherElement["elementName"] == "D_TNT":
                        result['D_TNT'] = weatherElement['elementValue']['value']
                break
    except Exception as e:
        result['Exception'] = str(e)

    return JsonResponse(result)
