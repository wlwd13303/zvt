##  1. 🔖5分钟用起来

### 1.1 安装

假设你已经在>=python3.6的环境中(建议新建一个干净的virtual env环境)
```
pip3 install zvt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

pip3 show zvt
```

如果不是最新版本
```
pip install --upgrade zvt  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

> 请根据需要决定是否使用豆瓣镜像源


###  1.2 进入ipython,初始化配置
```
#初次运行这一句会报错，并创建/home/xxx/zvt-home目录
In [1]: from zvt.domain import *
#退出并进入zvt-home路径
In [2]: exit
zvt-home路径下会有config.json，打开并并编辑以下配置
{
  "data_path": "/home/xxx/zvt-home/data",
  "db_engine": "xxx",
  "mysql_username": "xxx",
  "mysql_password": "xxx",
  "mysql_server_address": "xxx",
  "mysql_server_port": xxx,
  "db_name": "xxx"
}
```
###  1.2 进入ipython,开始使用接口获取数据
```
In [5]: from zvt.api import *
In [6]: df = get_kdata(entity_id='stock_sz_000338',start_timestamp='2019-01-01',limit=10)
In [7]: df
Out[7]: 
                                    id        entity_id  timestamp   provider    code  name level  open  close  high   low      volume     turnover change_pct turnover_rate
timestamp                                                                                                                                                                   
2019-01-02  stock_sz_000338_2019-01-02  stock_sz_000338 2019-01-02  joinquant  000338  潍柴动力    1d  7.33   7.17  7.34  7.16  22390100.0  164558000.0       None          None
2019-01-03  stock_sz_000338_2019-01-03  stock_sz_000338 2019-01-03  joinquant  000338  潍柴动力    1d  7.19   7.10  7.22  7.04  28278900.0  205391000.0       None          None
2019-01-04  stock_sz_000338_2019-01-04  stock_sz_000338 2019-01-04  joinquant  000338  潍柴动力    1d  7.04   7.21  7.22  7.02  21146800.0  154030000.0       None          None
2019-01-07  stock_sz_000338_2019-01-07  stock_sz_000338 2019-01-07  joinquant  000338  潍柴动力    1d  7.26   7.26  7.29  7.20  32106900.0  236955000.0       None          None
2019-01-08  stock_sz_000338_2019-01-08  stock_sz_000338 2019-01-08  joinquant  000338  潍柴动力    1d  7.27   7.26  7.27  7.20  16670800.0  122996000.0       None          None
2019-01-09  stock_sz_000338_2019-01-09  stock_sz_000338 2019-01-09  joinquant  000338  潍柴动力    1d  7.31   7.35  7.49  7.29  46791300.0  354013000.0       None          None
2019-01-10  stock_sz_000338_2019-01-10  stock_sz_000338 2019-01-10  joinquant  000338  潍柴动力    1d  7.38   7.41  7.47  7.33  26394400.0  199378000.0       None          None
2019-01-11  stock_sz_000338_2019-01-11  stock_sz_000338 2019-01-11  joinquant  000338  潍柴动力    1d  7.41   7.49  7.51  7.37  30223200.0  229583000.0       None          None
2019-01-14  stock_sz_000338_2019-01-14  stock_sz_000338 2019-01-14  joinquant  000338  潍柴动力    1d  7.51   7.59  7.72  7.50  51239800.0  397665000.0       None          None
2019-01-15  stock_sz_000338_2019-01-15  stock_sz_000338 2019-01-15  joinquant  000338  潍柴动力    1d  7.58   7.70  7.74  7.54  36695200.0  287000000.0       None          None
```

### 1.3 财务数据
```
In[11]: df = FinanceProfitAbility.query_data(
   ...:     filters=[FinanceProfitAbility.entity_id == 'stock_sz_000338'],
   ...:     start_timestamp='2019-01-01',
   ...:     columns=FinanceProfitAbility.important_cols())
   ...: 
In[12]: df
Out[12]: 
         entity_id    code  timestamp  gross_income_ratio  net_profit_ratio  roe_diluted   roe_avg  roe_wa  roe_ex_diluted  roe_ex_wa  net_roa      roa      roic
0  stock_sz_000338  000338 2019-03-31             21.6581           7.45955      6.15109   6.36367    6.37         5.81009        NaN  1.59827  2.01399  0.031833
1  stock_sz_000338  000338 2019-06-30             21.7486           7.58599     12.46700  12.93960   12.49        11.67710      11.72  3.15011  3.86992  0.057521
2  stock_sz_000338  000338 2019-09-30             22.0620           7.36273     16.46160  17.17520   17.20        15.03620        NaN  4.34924  5.36135  0.077958
3  stock_sz_000338  000338 2019-12-31             21.7983           6.82894     20.13300  21.54060   21.34        18.40330      19.58  5.38647  6.56748  0.099054
4  stock_sz_000338  000338 2020-03-31             22.4427           6.64547      4.35102   4.45518    4.46         3.84402        NaN  1.09881  1.27166  0.019876
5  stock_sz_000338  000338 2020-06-30             19.5830           6.03403      9.60890   9.96524    9.83         8.81446       9.02  2.29077  2.68109  0.043089
6  stock_sz_000338  000338 2020-09-30             19.4912           5.90404     14.38610  15.02010   15.02        13.83470        NaN  3.46740  4.12092  0.063748
```

>如果你不想使用使用默认的zvt_home目录,请设置环境变量ZVT_HOME再运行。

#### 数据的设计上是让provider来适配schema,而不是反过来，这样即使某provider不可用了，换一个即可，不会影响整个系统的使用。

> 项目中大部分的免费数据目前都是比较稳定的，且做过严格测试，特别是东财的数据，可放心使用


### 2.1 配置
在zvt_home目录中找到config.json进行配置,具体配置请联系运维人员。

> TODO:其他配置项用法

### 2.2 管理员维护更新数据

```

In [1]: from zvt.domain import *
In [2]: global_schemas
[zvt.domain.dividend_financing.DividendFinancing,
 zvt.domain.dividend_financing.DividendDetail,
 zvt.domain.dividend_financing.SpoDetail...]
```
整个系统的schema和其对应的recorders采取自注册的方式，global_schemas为系统支持的schema,而其对应的recorder以及如何更新数据，方法如下：
```
In [17]: FinanceFactor.recorders
Out[17]: [zvt.recorders.eastmoney.finance.china_stock_finance_factor_recorder.ChinaStockFinanceFactorRecorder]

In [18]: FinanceFactor.record_data(codes=['000338'])
FinanceFactor registered recorders:[<class 'zvt.recorders.eastmoney.finance.china_stock_finance_factor_recorder.ChinaStockFinanceFactorRecorder'>]
auth success  ( 如需说明文档请查看：https://url.cn/5oB7EOO，更多问题请联系JQData管理员，微信号：JQData02 )
INFO  MainThread  2019-12-15 18:03:35,493  ChinaStockFinanceFactorRecorder:recorder.py:551  evaluate_start_end_size_timestamps  entity_id:stock_sz_000338,timestamps start:2002-12-31 00:00:00,end:2019-09-30 00:00:00
INFO  MainThread  2019-12-15 18:03:35,509  ChinaStockFinanceFactorRecorder:recorder.py:556  evaluate_start_end_size_timestamps  latest record timestamp:2019-10-31 00:00:00
INFO  MainThread  2019-12-15 18:03:35,510  ChinaStockFinanceFactorRecorder:recorder.py:348  run  entity_id:stock_sz_000338,evaluate_start_end_size_timestamps result:None,None,0,None
INFO  MainThread  2019-12-15 18:03:35,510  ChinaStockFinanceFactorRecorder:recorder.py:357  run  finish recording <class 'zvt.domain.finance.FinanceFactor'> for entity_id:stock_sz_000338,latest_timestamp:None
已退出
```
* codes代表需要抓取的股票代码
* 不传入codes则是全市场抓取
* 所有的schema对应的数据更新，方法是一致的