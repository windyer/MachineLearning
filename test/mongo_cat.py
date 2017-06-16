# -*- coding:utf-8 -*-
import pymongo
import MySQLdb
import csv
import codecs

from go.util import DotDict
DATABASE = DotDict({
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'holytreetech.com',
    'db': 'card',
})
DATA_ADDR = ('localhost',10089)

client = pymongo.MongoClient(host = 'localhost', port = 13377)
card = client['card']
data={}
cat=[]
def mongo_data(date):
    coll = card["cat2currency_" + date]
    result = coll.find()
    for doc in result:
        if str(doc['user_id']) in data:
            data[str(doc['user_id'])] +=1
        else:
            data[str(doc['user_id'])] =1

def sql_data(user_id,cout):
    sql = "select cat_weight,nick_name from player where user_id = {0}".format(user_id)
    db = MySQLdb.connect(charset='utf8', **DATABASE)
    cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    records = cursor.fetchall()
    cursor.close()
    db.close()
    cat.append((user_id,records['nick_name'],cout,int(cout)*500+int(records['cat_weight']),records['cat_weight']))


date_list=['2017_06_15','2017_06_12','2017_06_13','2017_06_14']
for date in date_list:
    mongo_data(date)
for user_id in data:
    sql_data(user_id,data[user_id])

csvfile = file('csvtest.csv', 'wb')
csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile)
writer.writerow([u'user_id', u'nick_name',u'兑换前猫粮',u'兑换后猫粮',u'兑换数量'])
writer.writerows(cat)
csvfile.close()