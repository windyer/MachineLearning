#coding=utf-8
import requests
from tornado_test import ProStatus
requests.post("http://127.0.0.1:8080/get_chat",{'site':"chat",'user_id':u"12346",'text':u'3大声道asdasd'})
#ProStatus().makelines("sssssssssssss")