#coding=utf8
import hmac
import hashlib
import requests
s=requests.post("http://127.0.0.1:8000/upload/",{"a":1})
print s.content