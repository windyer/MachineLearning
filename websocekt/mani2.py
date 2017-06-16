import math
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import pymongo
import random
from collections import defaultdict
import csv

def addition_coefficient(history_recharge,today_recharge,is_first_charge):
    coef1 = math.log(1.0*history_recharge/1000+10,10)
    coef2 = math.log(1.0*today_recharge/200+10,10)
    if is_first_charge:
        coef3 = 2
    else:
        coef3 = 1
    coef = coef1*coef2*coef3
    return coef

def jackpot_config():
    data = {
    'TWO_RMB_COINS':[0,0,0,0,0,0,0,0.00018,0.0011],
    'SIX_RMB_COINS':[0,0,0,0,0,0,0.0001,0.00084,0.0011],
    'THIRTY_RMB_COINS':[0,0,0,0,0.0001,0.0002,0.0006,0.0031,0.0035],
    'FIFTH_RMB_COINS':[0,0,0,0.0001,0.0002,0.0005,0.001,0.0032,0.01],
    'HUNDRED_RMB_COINS':[0,0,0.0001,0.0002,0.0005,0.001,0.003,0.0058,0.011],
    'THREE_HUNDRED_RMB_COINS':[0.00001,0.0002,0.0004,0.0006,0.001,0.005,0.01,0.015,0.012],
    'MONKEY_FIFTY_RMB_BAGS':[0,0,0,0,0,0,0.0002,0.001,0.0022],
    'EIGHT_HUNDRED_RMB_BAGS':[0.00001,0.001,0.0015,0.003,0.005,0.01,0.02,0.03,0.04],
    }
    frame = DataFrame(data,index=[0.5,0.1,0.08,0.06,0.04,0.02,0.01,0.005,0.001],columns=['TWO_RMB_COINS','SIX_RMB_COINS','THIRTY_RMB_COINS','FIFTH_RMB_COINS','HUNDRED_RMB_COINS','THREE_HUNDRED_RMB_COINS','MONKEY_FIFTY_RMB_BAGS','EIGHT_HUNDRED_RMB_BAGS'])
    return frame

def random_pickup(index,probs):
    rd = random.random()
    total = 0
    counter = 0
    for p in probs:
        total+=p
        if rd <= total:
            break
        else:
            counter+=1
    if counter >= len(index):
        return 0
    else:
        return float(index[counter])

def jackpot_ratio(frame,package,coef):
    total_probability = frame[package].sum()
    if total_probability*coef <= 1:
        ratio = random_pickup(frame.index,frame[package].values)
    else:
        ratio = random_pickup(frame.index,frame[package].values/total_probability)
    return ratio

def charge_package_judge(item_id):
    if item_id in ['617','632','628','610','611']:
        return 'TWO_RMB_COINS'
    elif item_id in ['636','637','612','619','620','623','624','626','789','788','787','786','785','784','783','782','781','780','764','763','762','761','760','716','715','714','713','712','711','710']:
        return 'SIX_RMB_COINS'
    elif item_id in ['613','622','627','629','630','631','799','798','797','796','795','794','793','792','791','790','727','726','725','724','723','722','721','720']:
        return 'THIRTY_RMB_COINS'
    elif item_id in ['625','614']:
        return 'FIFTH_RMB_COINS'
    elif item_id in ['615','801','802','803','804','805','806','807','808','809','734','733','732','731','730']:
        return 'HUNDRED_RMB_COINS'
    elif item_id in ['616','819','818','817','816','815','814','813','812','811','810','744','743','742','741','740']:
        return 'THREE_HUNDRED_RMB_COINS'
    elif item_id in ['635','829','828','827','826','825','824','823','822','821','820','754','753','752','751','750']:
        return 'EIGHT_HUNDRED_RMB_BAGS'
    elif item_id in ['633','634','834','833','832','831','830','770','771','772']:
        return 'MONKEY_FIFTY_RMB_BAGS'

def simulation():
    frame = jackpot_config()
    charge_summary = defaultdict(float)
    f = open('C:/Users/dell/Desktop/charge.txt')
    line = f.readline()
    while line:
        temp = line.split(',')
        uid = temp[0]
        charge_amount = int(temp[1].strip())
        if charge_amount != 0:
            charge_summary[uid] = charge_amount
        line = f.readline()
    filename = 'result/jackpot_simulation.csv'
    csvfile = file(filename,'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['uid','price','ratio'])
    client = pymongo.MongoClient(host = 'localhost', port = 27017)
    mongodb = client['test3']
    table = 'charge_statistics_2016_10_26'
    coll = mongodb[table]
    today_recharge_summary = defaultdict(float)
    for doc in coll.find():
        user_id = str(doc['user_id'])
        price = doc['price']
        item_id = str(doc['item_id'])
        package = charge_package_judge(item_id)
        today_recharge_summary[user_id]+=price
        coef = addition_coefficient(charge_summary[user_id],today_recharge_summary[user_id]+price,user_id not in charge_summary)
        row = [user_id,price,jackpot_ratio(frame,package,coef)]
        writer.writerow(row)

def main():
    simulation()

if __name__ == '__main__':
    main()