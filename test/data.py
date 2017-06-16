import pymongo
import os
import datetime
colls = [
    'player_register',
    'player_login',
    'charge_statistics',
    #'player_online_period',
    #'single_charge_unit_summary',
    #'currency_liquidity',
    #'currency_liquidity_summary',
    #'currency_withdrawal',
    #'currency_issue',
    #'currency_withdrawal_summary',
    #'daily_summary',
]

begin = datetime.datetime(2016, 11, 1, 0, 0, 0, 0).date()
end = datetime.datetime(2016, 12, 1, 0, 0, 0, 0).date()

days = []
start = begin
while start < end:
    days.append(start.strftime("_%Y_%m_%d"))
    start += datetime.timedelta(days=1)
print days
client = pymongo.MongoClient(host = 'localhost', port = 13377)
mongodb = client['card']
for col in colls:
    for day in days:
        collection = col + day
        cmd = 'mongodump -h localhost:13377 -d card -c {0} -o .'.format(collection)
        print cmd
        os.system(cmd)
        print 'dump {0} ok!'.format(collection)


