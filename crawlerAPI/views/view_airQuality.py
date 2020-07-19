from django.http import JsonResponse
import json, requests

url = "https://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json"
re = requests.get(url, verify=False)
js_list = json.loads(re.content)


def post(request):
    result = {'result': 0}
    body = json.loads(request.body.decode(encoding='utf-8'))
    user_lon = body['Longitude']
    user_lat = body['Latitude']
    hy_list = []

    try:
        for js in js_list:
            hy = (float(js['Longitude']) - float(user_lon)) ** 2 + (float(js['Latitude']) - float(user_lat)) ** 2
            hy_list.append(hy)
        min_hy = min(hy_list)

        for js in js_list:
            if min_hy == (float(js['Longitude']) - float(user_lon)) ** 2 + (
                    float(js['Latitude']) - float(user_lat)) ** 2:
                result['result'] = 1
                result['SiteName'] = js['SiteName']
                result['County'] = js['County']
                result['AQI'] = js['AQI']
                result['Pollutant'] = js['Pollutant']
                result['AQIStatus'] = js['Status']
                result['PM10'] = js['PM10']
                result['PM2.5'] = js['PM2.5']
                result['WindSpeed'] = js['WindSpeed']
                result['WindDir'] = js['WindDirec']
                result['PM10Avg'] = js['PM10_AVG']
                result['PM2.5Avg'] = js['PM2.5_AVG']
                result['Date'] = js['PublishTime'].split(' ')[0]
                result['Time'] = js['PublishTime'].split(' ')[1]
                result['So2'] = js['SO2']
                result['Co'] = js['CO']
                result['O3'] = js['O3']
                result['So2Avg'] = js['SO2_AVG']
                result['PM2.5Status'] = 'test'

                break
    except Exception as e:
        result['Exception'] = str(e)

    return JsonResponse(result)



