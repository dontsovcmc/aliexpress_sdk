
import requests
from urllib import parse
from bs4 import BeautifulSoup
from waterius.influxdb import send
from aliexpress_api_client import AliExpress

import requests

# ОК

from datetime import datetime, timedelta
from top import api, appinfo
import pprint
import pytz

url = 'gw.api.taobao.com'
port = 80

appkey = ''
secret = ''

# https://oauth.aliexpress.com/authorize?response_type=token&client_id=30142523&state=1212&view=web&sp=ae
sessionkey = ''


def all_orders():
    req = api.AliexpressSolutionOrderGetRequest(url, port)
    req.set_app_info(appinfo(appkey, secret))

    req.param0 = {
        'create_date_start': (datetime.utcnow() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'),
        'page_size': 10,
        'current_page': 1
    }

    resp = req.getResponse(sessionkey)

    result = resp['aliexpress_solution_order_get_response']['result']

    for order in result['target_list']['order_dto']:
        #pprint.pprint(order)
        if order['order_status'] == 'WAIT_SELLER_SEND_GOODS':
            ts = datetime.strptime(order['gmt_create'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc)

            fields = []
            fields.append((ts+timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S'))
            fields.append(order['order_id'])

            for p in order['product_list']['order_product_dto']:
                fields.append(p['product_name'])
                fields.append(p['product_count'])
                fields.append(p['total_product_amount']['amount'])

            out = ';'.join([str(f) for f in fields])

            print(out)


    #pprint.pprint(resp['aliexpress_solution_order_get_response']['result'])

    # fund_status PAY_SUCCESS
    # order_status WAIT_SELLER_SEND_GOODS


if __name__ == '__main__':
    all_orders()



