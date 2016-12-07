class Bunch(object):
    def __init__(self,**kwd):
        self.__dict__.update(kwd)

test = Bunch(a=1,b=2,c=3)
test.c=4
#print test.a,test.c

a=["B","a","c","D"]
b=sorted(a,key=str.lower)
#print b

from operator import itemgetter
dic={"a":3,"b":1,"c":8}
dic2 = sorted(dic.iteritems(),key=itemgetter(1),reverse=False)
print dic2
#[('b', 1), ('a', 3), ('c', 8)]
x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':40}]
sorted_x = sorted(x, key=itemgetter('age'))
print sorted_x
#[{'age': 10, 'name': 'Bart'}, {'age': 39, 'name': 'Homer'}]

