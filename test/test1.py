import requests
import threading
import time
import os
import json
def up(a,**_):
    print a
    files = {'image': open("1.jpg".format(a), 'rb')}
    resp = requests.post(url="http://127.0.0.1:8000",files=files)
    s=resp.content
    print resp.content,type(resp.content)
    print json.loads(s,strict=False)
threads = []
for i in range(1):
    s=str(i)
    t1 = threading.Thread(target=up,args=(s))
    threads.append(t1)
print time.time()
for t in threads:
    #t.setDaemon(True)
    t.start()
print time.time()
