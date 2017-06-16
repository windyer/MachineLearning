# coding=utf-8
import pymongo
import re
import time
import datetime
client = pymongo.MongoClient(host='114.215.129.89', port=13377)

mongodb = client['card']


def increment_currency(user_id, date, start, end):
    info2 = []
    date = date.replace("-", "_")
    info = u"{0} player({1}) increment currency:{2} by {3}"
    coll = mongodb["currency_issue_" + date]
    result = coll.find({'user_id': user_id})
    add_currency = []
    total = 0
    for i in result:
        x = time.localtime(i['timestamp'] / 1000)
        if start < time.strftime(
                '%H:%M:%S',
                x) and end > time.strftime(
                '%H:%M:%S',
                x):
            i['time'] = time.strftime('%Y-%m-%d %H:%M:%S', x)
            add_currency.append(i)
            log = info.format(i["time"], user_id, i["delta"], i["reason"])
            total += i["delta"]
            info2.append(log)
    info2.sort()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~increment currency in mongo \n"
    fp = open("test.txt", "w")
    fp.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~increment currency in mongo \n")
    for log in info2:
        fp.write(log + "\n")
        print log
    print "player({0}) increment currency total:{1} in {2}-{3}".format(user_id, total, start, end)
    fp.write(
        "player({0}) increment currency total:{1} in {2}-{3} \n".format(user_id, total, start, end))
    fp.close()
    return info2


def consume_currency(user_id, date, start, end):
    info2 = increment_currency(int(user_id), date.replace("-","_"), start, end)
    info = []
    if date == str(datetime.date.today()):
        lobby_log = "~/qmbzw.server/log/lobby.log"
        three_log = "~/qmbzw.server/log/three.log"
        fruit_log = "~/qmbzw.server/log/fruit.log"
        db_log = "~/qmbzw.server/log/db.log"
        game_log = "~/qmbzw.server/log/game1.log"
    else:
        lobby_date = datetime.datetime.strptime(
            date, "%Y-%m-%d") + datetime.timedelta(days=1)
        lobby_log = "/home/windyer/Downloads/mnt/log/lobby.log." + \
            str(lobby_date)[:10]
        three_log = "/home/windyer/Downloads/mnt/log/three.log." + date
        fruit_log = "/home/windyer/Downloads/mnt/log/fruit.log." + date
        db_log = "/home/windyer/Downloads/mnt/log/db.log." + date
        game_log = "/home/windyer/Downloads/mnt/log/game1.log." + date
    start_time = date + " " + start
    end_time = date + " " + end
    print start_time, end_time
    with open(lobby_log) as file:
        print "~~~~~~~~~~~~~~~~~~start lobby"
        for line in file:
            if start_time > line or end_time < line:
                continue
            if "lobby.PurchaseItem:27" in line and user_id in line:
                user = re.findall(r"\[user\|(.+?)\]", line)
                item_id = re.findall(r"item_id': (.+?),", line)
                currency = re.findall(r"currency': (.+?),", line)
                log = "{0} player({1}) buy item_id({2}) residue currency {3} ".format(
                    line[1:20], user[0], item_id[0], currency[0])
                print log
                info.append(log)
    with open(three_log) as file:
        print "~~~~~~~~~~~~~~~~~~start three"
        for line in file:
            if start_time > line or end_time < line:
                continue
            if "LoseThreeRequest" in line and user_id in line:
                user = re.findall(r"user_id': (.+?),", line)
                lose_currency = re.findall(r"lose_currency': (.+?)L,", line)
                lose_bank_currency = re.findall(
                    r"lose_bank_currency': (.+?)L,", line)
                log = "{0} plyer({1})  lose currency {2} and lose bank_currency {3} in three".format(
                    line[:19], user[0], lose_currency[0], lose_bank_currency[0])
                print log
                info.append(log)
            if "WinThreeRequest" in line and user_id in line:
                user = re.findall(r"user_id': (.+?),", line)
                gain_currency = re.findall(r"gain_currency': (.+?)L,", line)
                log = "{0} plyer({1})  win currency {2} in three".format(
                    line[:19], user[0], gain_currency[0])
                print log
                info.append(log)
            if "session_currency" in line and "[user|{0}]".format(
                    user_id) in line and "three.PlayerAgent" in line:
                session_currency = re.findall(
                    r"session_currency': (.+?)L", line)
                log = "{0} plyer({1}) session currency {2}".format(
                    line[:19], user_id, "".join(session_currency))
                print log
                info.append(log)
            if "peer_send_red_envelope" in line and user_id in line:
                red_envelope = re.findall(
                    r"delta_currency': (.+?)L", line)
                log = "{0} plyer({1}) send red envelope {2}".format(
                    line[:19], user_id, "".join(red_envelope))
                print log
                info.append(log)
            if "open_red_envelope" in line and "[user|{0}]".format(
                    user_id) in line:
                red_envelope = re.findall(
                    r"delta_currency': (.+?)L", line)
                log = "{0} plyer({1}) open red envelope {2}".format(
                    line[:19], user_id, "".join(red_envelope))
                print log
                info.append(log)
    with open(fruit_log) as file:
        print "~~~~~~~~~~~~~~~~~~start fruit"
        for line in file:
            if start_time > line or end_time < line:
                continue
            if "LoseFruitRequest" in line and user_id in line:
                user = re.findall(r"user_id': (.+?),", line)
                lose_currency = re.findall(r"lose_currency': (.+?)L,", line)
                log = "{0} plyer({1})  lose currency {2} in fruit".format(
                    line[:19], user[0], lose_currency[0])
                print log
                info.append(log)
            if "WinFruitRequest" in line and user_id in line:
                user = re.findall(r"user_id': (.+?),", line)
                gain_currency = re.findall(r"gain_currency': (.+?)L,", line)
                log = "{0} plyer({1})  win currency {2} in fruit".format(
                    line[:19], user[0], gain_currency[0])
                print log
                info.append(log)
            if "session_currency" in line and "[user|{0}]".format(
                    user_id) in line and "fruit_end_trace" in line:
                session_currency = re.findall(
                    r"session_currency': (.+?)L", line)
                log = "{0} plyer({1}) session currency {2}".format(
                    line[:19], user_id, "".join(session_currency))
                print log
                info.append(log)
            if "peer_send_red_envelope" in line and user_id in line:
                red_envelope = re.findall(
                    r"delta_currency': (.+?)L", line)
                log = "{0} plyer({1}) send red envelope {2}".format(
                    line[:19], user_id, "".join(red_envelope))
                print log
                info.append(log)
            if "open_red_envelope" in line and "[user|{0}]".format(
                    user_id) in line:
                red_envelope = re.findall(
                    r"delta_currency': (.+?)L", line)
                log = "{0} plyer({1}) open red envelope {2}".format(
                    line[:19], user_id, "".join(red_envelope))
                print log
                info.append(log)
    with open(game_log) as file:
        print "~~~~~~~~~~~~~~~~~~start game"
        for line in file:
            if "[" + start_time > line or "[" + end_time < line:
                continue
            if "lose round with" in line and "[user|{0}]".format(
                    user_id) in line:
                session_currency = re.findall(r"currency\|(.+?)\]", line)
                log = "{0} plyer({1}) session currency {2}".format(
                    line[1:19], user_id, "".join(session_currency))
                print log
                info.append(log)
            if "win round with" in line and "[user|{0}]".format(
                    user_id) in line:
                session_currency = re.findall(r"currency\|(.+?)\]", line)
                log = "{0} plyer({1}) session currency {2}".format(
                    line[1:19], user_id, "".join(session_currency))
                print log
                info.append(log)
            if "peer_send_red_envelope" in line and user_id in line:
                red_envelope = re.findall(
                    r"delta_currency': (.+?)L", line)
                log = "{0} plyer({1}) send red envelope {2}".format(
                    line[:19], user_id, "".join(red_envelope))
                print log
                info.append(log)
            if "open_red_envelope" in line and "[user|{0}]".format(
                    user_id) in line:
                red_envelope = re.findall(
                    r"delta_currency': (.+?)L", line)
                log = "{0} plyer({1}) open red envelope {2}".format(
                    line[:19], user_id, "".join(red_envelope))
                print log
                info.append(log)
    with open(db_log) as file:
        print "~~~~~~~~~~~~~~~~~~start db"
        for line in file:
            if "["+start_time > line or "["+end_time < line:
                continue
            if "lose_currency" in line and user_id in line and "LoseRoundRequest" in line:
                lose_currency = re.findall(r"lose_currency': (.+?)L", line)
                log = "{0} plyer({1})  lose currency {2} in game".format(
                    line[1:19], user_id, "".join(lose_currency))
                print log
                info.append(log)
            if "gain_currency" in line and user_id in line and "WinRoundRequest" in line:
                gain_currency = re.findall(r"gain_currency': (.+?)L", line)
                log = "{0} plyer({1})  win currency {2} in game".format(
                    line[1:19], user_id, "".join(gain_currency))
                print log
                info.append(log)
    info.extend(info2)
    info.sort()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~log result\n"
    fp = open("test.txt", "a")
    fp.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~log result\n")
    for log in info:
        fp.write(log + "\n")
        print log
    fp.close()
consume_currency("11090905", "2016-12-28", "00:00:00", "24:00:00")
