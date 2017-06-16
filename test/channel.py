# -*- coding:utf-8 -*-
import pymongo
import datetime
import time

"""
c_file = open('channels.conf')
line = c_file.readline().strip()
temp = line.split(' ')
channels = []
for c in temp:
    if c == "":
        continue
    channels.append(c)
"""
channels = ['lenovo_duowan',]
client = pymongo.MongoClient(host = 'localhost', port = 13377)
card = client['card']
#coll = card['daily_summary']

begin = datetime.datetime(2016, 6, 1, 0, 0, 0, 0).date()
begin_timestamp = time.mktime(begin.timetuple()) * 1000
end = datetime.datetime(2016, 6, 12, 0, 0, 0, 0).date()
end_timestamp = time.mktime(end.timetuple()) * 1000

datas = {}

RETENTION_SUMMARY = {
    'report_table_headers': [
        #[u'新增用户(人)', 'dnu'],
        [u'次日留存(%)', 'rr2'],
        #[u'三日留存(%)', 'rr3'],
        #[u'七日留存(%)', 'rr7'],
        #[u'十日留存(%)', 'rr10'],
        #[u'十五日留存(%)', 'rr15'],
        #[u'二十日留存(%)', 'rr20'],
        #[u'三十日留存(%)', 'rr30'],
    ],
    'db': 'card',
    'collection': 'retention_summary',
}

SILENT_USERS_SUMMARY = {
    'report_table_headers': [
        #[u'新增用户(人)', 'dnu'],
        [u'沉默用户(人)', 'dsnu'],
        #[u'沉默用户占比(%)', 'dsnur'],
        #[u'沉默用户次日留存(%)', 'snurr2'],
        #[u'沉默付费用户', 'snucu'],
    ],
    'db': 'card',
    'collection': 'silent_users_summary',
}

DAILY_SUMMARY = {
    'report_table_headers': [
        [u'新增用户(人)', 'dnu'],
        #[u'登录用户(人)', 'dlu'],
        #[u'活跃用户(登录-新增)(人)', 'dau'],

        #[u'充值用户(人)', 'dcu'],
        [u'充值金额(元)', 'dcr'],

        #[u'新充值用户(人)', 'dncu'],   # daily new charge user
        #[u'新玩家充值金额(元)', 'dncr'],   # daily new user charge revenue

        #[u'活跃玩家付费率(%)', 'aucr'], # activated users charge ratio

        #[u'新玩家人均充值(元)', 'arpnu'], # averaged revenue per paying user
        #[u'付费玩家人均充值(元)', 'arppu'], # averaged revenue per paying user
        #[u'活跃玩家人均充值(元)', 'arpau'], # averaged revenue per active user
    ],
    'db': 'card',
    'collection': 'daily_summary',
}

#fields = ['dnu', 'dcr']

stats = [RETENTION_SUMMARY, DAILY_SUMMARY,]

for st in stats:
    coll = client[st['db']][st['collection']]
    result = coll.find({"channel":{"$in":channels}, 'timestamp':{'$lt': end_timestamp, '$gte': begin_timestamp}})
    for doc in result:
        t = doc['timestamp']
        c = doc['channel']
        if c not in datas:
            datas[c] = {}
        if t not in datas[c]:
            datas[c][t] = {}
            for f in st['report_table_headers']:
                datas[c][t][f[1]] = 0
        for f in st['report_table_headers']:
            if f[1] not in datas[c][t]:
                datas[c][t][f[1]] = 0
            if f[1] in doc:
                datas[c][t][f[1]] += float(doc[f[1]])

for c in datas:
    out = open(c + ".txt", 'w')
    msg = "time"
    for st in stats:
        for f in st['report_table_headers']:
            msg += "\t" + f[0].encode('utf-8')
    msg += "\r\n"
    out.write(msg)

    days = sorted(datas[c])
    for t in days:
        timeArray = time.localtime(t/1000)
        msg = time.strftime("%Y-%m-%d", timeArray)
        for st in stats:
            for f in st['report_table_headers']:
                if f[1] not in datas[c][t]:
                    msg += "\t0"
                else:
                    msg += "\t" + str(datas[c][t][f[1]])
        msg += "\r\n"
        out.write(msg)
    out.close()



