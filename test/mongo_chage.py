# coding=utf-8

import MySQLdb
from collections import defaultdict

from go.util import DotDict
import go.client

from card.api.db.service.player_service import PlayerService

DATABASE = DotDict({
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'holytreetech.com',
    'db': 'card',
})

DATA_ADDR = ('localhost',10089)

sql ="select A.user_id,A.charge_money,A.channel,B.channel from player as A,player_extra as B where A.charge_money>0 and B.channel='sj05'"

db = MySQLdb.connect(charset='utf8', **DATABASE)
cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
cursor.execute(sql)
records = cursor.fetchall()
cursor.close()
db.close()
actived_players = []
for item in records:
    print "{0} {1} {2} {3}".format(item['user_id'],item['charge_money'],item['channel'],item['B.channel'])

