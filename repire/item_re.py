# coding=utf-8

import MySQLdb
from collections import defaultdict
import time
from go.util import DotDict
import go.client
import redis
import json
DATABASE = DotDict({
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'holytreetech.com',
    'db': 'card_logger',
})

DATA_ADDR = ('localhost',10089)

class GetData(object):

    def _excute_sql(self, sql):
        records = []
        db = MySQLdb.connect(charset='utf8', **DATABASE)
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        db.close()

        return records

    def _get_candidate_ids(self):
        r = redis.Redis(host='localhost', port=13380, db=2)
        qmBZW = [617,
                 610,
                 660,
                 632,
                 633,
                 634,
                 636,
                 637,
                 671,
                 672,
                 673,
                 674,
                 675,
                 681,
                 667,
                 676,
                 677,
                 678,
                 679,
                 691,
                 692,
                 693,
                 694,
                 695,
                 696,
                 ]
        #sql = 'select A.user_id, A.currency, B.created_time from player as A, player_extra as B where A.charge_money=0 and A.is_active=1 and B.channel="toutiao_cpc_v201_005" and B.networking="WiFi-2G" and B.vender="Coolpad" and B.resolution="800x480" and A.user_id=B.user_id'
        #sql = 'select A.user_id, A.currency, B.channel, B.created_time, B.last_login_time from player as A, player_extra as B where A.charge_money=0 and A.is_active=1 and (B.channel="lenovo" or B.channel="daiji_kuku") and A.user_id=B.user_id and B.last_login_time>"2016-11-25 00:00:00" and B.created_time>"2016-11-01 00:00:00"'
       # sql = 'select B.user_id, B.channel, B.created_time, C.total_win_rounds from  player_extra as B,player_profile as C where B.channel="kuku_001" and B.user_id=C.user_id and B.created_time>"2017-4-17 00:00:00" and C.total_win_rounds=0'
        sql = 'select appuserid,item_id ,transtime from iapppay_charge_log WHERE result<=0 and transtime >"2016-11-19"'
        sql2 = 'select ext2,ext1 ,created_time from skypay_charge_log WHERE realAmount>0 and created_time >"2016-11-19"'

        records = self._excute_sql(sql)

        players = []
        out = open('user_item.txt', 'w')
        for item in records:

            item['transtime'] = int(time.mktime(time.strptime(item['transtime'],'%Y-%m-%d %H:%M:%S')))

            if item['item_id'] in qmBZW:
                print item
                #table = 'ChargeStatus:{0}'.format(item['appuserid'])
                #data = {"count":1,"last_time_stamp":item['transtime']}
                #r.hset(table, item['item_id'], json.dumps(data))
           # out.write('{0},{1},{2},{3}, {4}, {5}\n'.format(item['user_id'], item['charge_money'], item['currency'], item['created_time'], item['channel'], item['last_login_time']))
                out.write(str(item)+'\n')
                players.append(item)

        records2 = self._excute_sql(sql2)

        for item in records2:

            item['created_time'] = int(time.mktime(time.strptime(str(item['created_time']), '%Y-%m-%d %H:%M:%S')))

            if int(item['ext1']) in qmBZW:
                print item
                #table = 'ChargeStatus:{0}'.format(item['ext2'])
                #data = {"count": 1, "last_time_stamp": item['created_time']}
                #r.hset(table, item['ext1'], json.dumps(data))
                # out.write('{0},{1},{2},{3}, {4}, {5}\n'.format(item['user_id'], item['charge_money'], item['currency'], item['created_time'], item['channel'], item['last_login_time']))
                out.write(str(item) + '\n')
                players.append(item)

        return players


    def get_data(self):
        candidate_uses = self._get_candidate_ids()


if __name__ == '__main__':
    corpse = GetData()
    corpse.get_data()