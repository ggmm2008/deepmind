# -*- coding:utf-8 -*-  

import requests 

def requestData():
    key={'address':'双成二路','city':'成都'}
    txt='http://restapi.amap.com/v3/geocode/geo?key=5a65393af609a75927a1809fd3be56a1'
    r = requests.get(txt,params=key)
    print r.text
    return r