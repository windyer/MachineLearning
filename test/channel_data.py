# -*- coding:utf-8 -*-
import pymongo
import datetime
import time

c_file = open('channels.conf')
line = c_file.readline().strip()
temp = line.split(' ')
channels = []
for c in temp:
    if c == "":
        continue
    channels.append(c)

client = pymongo.MongoClient(host = 'localhost', port = 13377)
card = client['card']
#coll = card['daily_summary']

begin = datetime.datetime(2016, 11, 1, 0, 0, 0, 0).date()
end = datetime.datetime(2016, 12, 1, 0, 0, 0, 0).date()

datas = {}
"""
field_infos = {'dnu':u'新增用户(人)',
          'dlu':u'登录用户(人)',
          'dau':u'活跃用户(登录-新增)(人)',
          'dcu':u'充值用户(人)',
          'dcr':u'充值金额(元)',
          'dncu':u'新充值用户(人)',
          'dncr':u'新玩家充值金额(元)',
          'aucr':u'活跃玩家付费率(%)',
          'rr2':u'次日留存',
          }
"""
field_infos = {'dnu':u'新增用户(人)',
          'dlu':u'登录用户(人)',
          'dau':u'活跃用户(登录-新增)(人)',
          'dcu':u'充值用户(人)',
          'dcr':u'充值金额(元)',
          'dncu':u'新充值用户(人)',
          'dncr':u'新玩家充值金额(元)',
          'aucr':u'活跃玩家付费率(%)',
          'rr2':u'次日留存',
          'arpnu':u'新玩家人均充值(元)',
          'arppu':u'付费玩家人均充值(元)',
          'arpau':u'活跃玩家人均充值(元)',
          }
total_fields = ['dnu', 'dncu', 'aucr', 'rr2']
#fields = ['dnu', 'dcr', ]
fields = ['dnu', 'dlu', 'dau', 'dcu', 'dcr', 'dncu', 'dncr', 'aucr', 'arpnu', 'arppu', 'arpau', ]

start = begin
while start < end:
    day = start.strftime("_%Y_%m_%d")
    print day
    coll = card['daily_summary' + day]
    start += datetime.timedelta(days=1)
    result = coll.find({"channel":{"$in":channels}, 'version':'all_version'})
    for doc in result:
        c = doc['channel']
        if c not in datas:
            datas[c] = {}
        if day not in datas[c]:
            datas[c][day] = {}
            for f in fields:
                datas[c][day][f] = 0
        for f in fields:
            if f in doc:
                datas[c][day][f] += float(doc[f])

for c in datas:
    out = open(c + ".txt", 'w')
    msg = "time"
    for f in fields:
        msg += "\t" + field_infos[f].encode('utf-8')
    msg += "\r\n"
    out.write(msg)
    days = sorted(datas[c])
    for day in days:
        msg = day
        for f in fields:
            v = 0
            if f in datas[c][day]:
                v = datas[c][day][f]
            msg += "\t" + str(v)
        msg += "\r\n"
        out.write(msg)
    out.close()



