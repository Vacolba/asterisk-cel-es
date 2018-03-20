import sys
import time
import pprint
import requests


def send_to_es(es_url, data):
    index = time.strftime("%Y.%m.%d", time.localtime(data['eventtime']))
    es_url = "{0}/asterisk-{1}/cel".format(es_url, index)
    req = requests.post(es_url, json=data)
    if req.status_code != 201:
        pprint.pprint(data)
        pprint.pprint(req.status_code)
        pprint.pprint(req.text)
        sys.exit(-1)
