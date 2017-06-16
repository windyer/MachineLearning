import redis
from go.task import Task
from go.containers.containers import (SortedSet, List, Hash)
from card.db.task.redis_task import (UpdateFruitWeekIncomeRankTask,
                                     UpdateCurrencyRankTask, UpdateDailyIncomeRankTask, UpdateGiftRankTask,
                                     UpdateRedEnvelopeMonthlySendRankTask, UpdateChargeRankTask)
import pymongo
#20429403
r = redis.Redis(host='localhost', port=13380,db=2)

class RedisTask(Task):

    def __init__(self, user_id, key):
        self._user_id = user_id
        re = redis.Redis(**settings.PERSIST_REDIS)
        self._zorted = SortedSet(key, db=re)
        super(RedisTask, self).__init__()

    @property
    def affinity(self):
        return self._user_id

    def pre_run(self):
        super(RedisTask, self).pre_run()
        self.logger.debug('[task|%s] [user|%d] pre [task|%s]', self.tid, self._user_id, self.tid)

    def post_run(self):
        super(RedisTask, self).post_run()
        runtime = self._end_time - self._start_time
        self.logger.debug('[user|%d] post run [task|%s] [time|%f]', self._user_id, self.tid, runtime)


class UpdateCurrencyRankTask(RedisTask):

    def __init__(self, user_id, currency):
        self._currency = currency
        super(UpdateCurrencyRankTask, self).__init__(user_id, Rank.CURRENCY)

    def run(self,user_id,currency):
        self._zorted.add(user_id, currency)