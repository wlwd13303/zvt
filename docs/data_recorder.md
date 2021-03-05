## 1. 财报数据更新

定时任务的运行，方法很多，下面是一个参考脚本:
```
# -*- coding: utf-8 -*-
import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler

from zvt import init_log
from zvt.domain import *

logger = logging.getLogger(__name__)

sched = BackgroundScheduler()


# 自行更改定时运行时间
@sched.scheduled_job('cron', hour=2, minute=00)
def run():
    while True:
        try:
            FinanceFactor.record_data()
            BalanceSheet.record_data()
            IncomeStatement.record_data()
            CashFlowStatement.record_data()
            break
        except Exception as e:
            logger.exception('finance recorder error:{}'.format(e))
            time.sleep(60)


if __name__ == '__main__':
    init_log('eastmoney_finance_recorder.log')

    run()

    sched.start()

    sched._thread.join()
```

然后可将该脚本作为后台任务一直运行，ubuntu的参考命令如下:

```
nohup python examples/recorders/finance_recorder.py  >/dev/null 2>&1 &
```