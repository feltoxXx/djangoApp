from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from hiveengine.api import Api
import json

URLrpc = "https://engine.rishipanthee.com/contracts"

api = Api()


def index(request):
    
    offset = 0
    result = []
    hk_bang = api.get_history("feltoxxx", "BUDS",500,offset)
    # result.append(hk_bang)
    suma = 0
    for item in hk_bang:
        if item["to"]=="null":
            break
        result.append(item)
    n = 0

    # while len(hk_bang) == 500:
    #     offset = offset + 500
    #     hk_bang = api.get_history("hk-dev", "BUDS",500,offset)
    #     for item in hk_bang:
    #         result.append(item)
            # if result[item]["to"]=="null":
            #   break
    #     rewards = get_rewards_from_last_week(account, rewards, offset=offset)
    #     offset += 1000
    # # for item in hk_bang:
    # #     if not item['to'] == 'null':
    # #         print(float(item['quantity']))
    # #         suma = float(item['quantity']) + float(suma)
    # #     else:
    # #       print('quemado en el bloque', item['blockNumber'], datetime.fromtimestamp(item['timestamp']).strftime("%Y-%m-%d %H:%M:%S"))
    # #       print('buds desde la quema', suma)
    # #       print(datetime.fromtimestamp(item['timestamp']).strftime("%Y-%m-%d %H:%M:%S"))
    # #       print(item)
    # #       break
    # return result
    return HttpResponse(json.dumps(result), content_type="application/json")