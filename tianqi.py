# -*- coding: utf-8 -*-
import json
import gzip
import urllib.request
from urllib import parse
import time
def search(city):
    try:
        city_name = parse.quote_plus(city)
        only_now = parse.quote_plus('1')
        appid = "63121ece48ccb9f3495430c926a6fae0"
        url = "https://api.shenjian.io/weather/city/?appid=" + appid + "&city_name=" + city_name + "&only_now=" + only_now

        request = urllib.request.Request(url,

                                         headers={

                                             "Accept-Encoding": "gzip",

                                         })

        response = urllib.request.urlopen(request)
        gzipFile = gzip.GzipFile(fileobj=response)
        a = gzipFile.read().decode('utf-8')
        print(a)

        data = json.loads(a)
    except Exception as e:
        print(e)
    return data

def show(data):
    tplt = "{:4}\t{:16}"
    date = data.get('data')
    for key, valus in date.items():
        print(tplt.format(key, valus))

if __name__ == '__main__':
    while True:
        city = input('请输入要查询的城市：')
        show(search(city))
        time.sleep(5)
        out = input('是否继续查询（停止请按1）：')
        if out == '1':
            break