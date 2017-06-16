import MySQLdb
from collections import defaultdict

from go.util import DotDict
import go.client

from card.api.db.service.player_service import PlayerService
DATA_ADDR = ('localhost',10089)
def _deactive_user(user_id):
    service_proxy = go.client.create_service_proxy(DATA_ADDR)
    player_service = PlayerService(service_proxy)
    player_service.update_profile(user_id=user_id, is_active=False)
with open("") as file:
    for line in file:
        try:
            _deactive_user(int(line))
            print "deactive " + line +"OK!"
        except:
            print "deactive " + line + "FALSE!"