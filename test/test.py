
import MySQLdb

from go.util import DotDict

DATABASE = DotDict({
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'holytreetech.com',
    'db': 'card',
    'cursorclass' : 'MySQLdb.cursors.DictCursor',
})

DATA_ADDR = ('localhost',10089)
sql = 'select user_id,currency, charge_money from player WHERE user_id ={0}'

records = []
db = MySQLdb.connect(charset='utf8', **DATABASE)
cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
with open("user_list") as file:
    for line in file:
        cursor.execute(sql.format(int(line)))
        result = cursor.fetchall()
        for i in result:
            print i
            records.append(i)
cursor.close()
db.close()
actived_players = []
out = open('user.txt', 'w')
for item in records:
    s="user:{0}  currency:{1}  charge_money:{2}".format(item['user_id'],item['currency'],item['charge_money'])
    out.write(s)
out.close()



