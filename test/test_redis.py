import csv
csvfile = file('csvtest.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['id', 'url', 'keywords'])
data = [
  ('1', 'http://www.xiaoheiseo.com/', 'aaa'),
  ('2', 'http://www.baidu.com/', 'bbb'),
  ('3', 'http://www.jd.com/', 'ccc')
]
writer.writerows(data)
csvfile.close()