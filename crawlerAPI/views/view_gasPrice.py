from django.http import JsonResponse
import json, requests

url = "https://www.cpc.com.tw/GetOilPriceJson.aspx?type=TodayOilPriceString"
re = requests.get(url, verify=False)
js = json.loads(re.content)


def post(request):
    result = {'result': 0}
    body = json.loads(request.body.decode('utf-8'))
    type = body['Type']

    try:
        if type == 'All':
            result['result'] = 1
            result['Unleaded'] = js['sPrice1']
            result['Super'] = js['sPrice2']
            result['Supreme'] = js['sPrice3']
            result['AlcoholGas'] = js['sPrice4']
            result['Diesel'] = js['sPrice5']
            result['LiquefiedGas'] = js['sPrice6']
        elif type == 'Unleaded':
            result['result'] = 1
            result['Unleaded'] = js['sPrice1']

        elif type == 'Super':
            result['result'] = 1
            result['Super'] = js['sPrice2']

        elif type == 'Supreme':
            result['result'] = 1
            result['Supreme'] = js['sPrice3']

        elif type == 'AlcoholGas':
            result['result'] = 1
            result['AlcoholGas'] = js['sPrice4']

        elif type == 'Diesel':
            result['result'] = 1
            result['Diesel'] = js['sPrice5']

        elif type == 'LiquefiedGas':
            result['result'] = 1
            result['LiquefiedGas'] = js['sPrice6']

    except Exception as e:
        result['Exception'] = str(e)

    return JsonResponse(result)
