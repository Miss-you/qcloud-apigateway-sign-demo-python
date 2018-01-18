# -*- coding: utf-8 -*-

import requests
import datetime
from hashlib import sha1
import hmac
import base64
from com.qcloudapigateway.auth import sign


#r = requests.get('https://github.com/timeline.json')
#print r 
#print r.text

SecretId = 'AKIDgz33go7zufbgrt6azbakwbx7tx0jampv84kz'
SecretKey = 'lCIC0ZQhtcI5u36Lojuh2bnOBqaKy6r5FF4Qc1'
url = 'http://service-3mm3bc6g-1251762227.ap-guangzhou.apigateway.myqcloud.com/release/yousa'

#header = {}
header = { 'Host':'service-3mm3bc6g-1251762227.ap-guangzhou.apigateway.myqcloud.com',  
            'Accept': 'text/html, */*; q=0.01',  
            'X-Requested-With': 'XMLHttpRequest',  
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',  
            'Accept-Encoding': 'gzip, deflate, sdch',  
            'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'  
}

Source = 'yousali'
sign, dateTime = sign.getSimpleSign(Source, SecretId, SecretKey)
header['Authorization'] = sign
header['Date'] = dateTime
header['Source'] = Source

print header 

r = requests.get(url, headers=header)
print r
print r.text