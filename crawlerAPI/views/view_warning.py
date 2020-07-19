from django.http import JsonResponse
import json, requests

url = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/W-C0033-001?Authorization=CWB-242E2AA6-F542-43E1-973D-9A0A4DBB7E5E&downloadType=WEB&format=JSON"
re = requests.get(url, verify=False)
js_list = json.loads(re.content)['cwbopendata']["dataset"]["location"]


def post(request):
    result = {'result': 0}
    body = json.loads(request.body)
    body_city = body['City']

    try:
        for js in js_list:
            if body_city in js['locationName']:
                result['result'] = 1
                result['locationName'] = js['locationName']

                hazardConditions = js['hazardConditions']

                if hazardConditions is dict:  # 有警報
                    result['hazardConditions'] = js['hazards']['info']['phenomena']
                else:
                    result['hazardConditions'] = "None"
                break

    except Exception as e:
        result['Exception'] = str(e)

    return JsonResponse(result)

