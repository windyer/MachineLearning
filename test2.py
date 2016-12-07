import MySQLdb.cursors
conn = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='holytreetech.com',
    db='card',
    port=3306,
    cursorclass=MySQLdb.cursors.DictCursor)
cur = conn.cursor()
count = cur.execute('select * from player')
result = cur.fetchall()
for row in result:
    print type(row)
#>>> <type 'dict'>


a=None
if a!=None and int(a):
    print "aaaa"