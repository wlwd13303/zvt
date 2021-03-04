## 1. 数据是什么？

zvt对量化数据进行了简洁统一的抽象：数据就是 **投资标的** 在**某时间点(段)** 所**发生的事情**的描述。

其中，投资标的，叫**entity**；时间点(段)，叫**timestamp**；事情的描述根据事情的不同而具有不同的**属性**。

整体结构如下:
<p align="center"><img src='./imgs/domain.png'/></p>

### 1.1 投资标的(entity)

首先，我们得有投资标的。

而在整个市场里，投资标的一定会有三个属性:

* **证券类型(entity_type)**

股票(stock)，数字货币(coin)，指数(index)，场内基金(etf)，场外基金(fund)等

* **交易所(exchange)**

上海证券交易所(sh)，深圳证券交易所(sz)，*香港*联交所证券(hk)，纳斯达克证券交易所(o)，美国证券交易所(a)，美国纽约证券交易所(n)等

* **代码(code)**

投资标的编码，A股中的000338,601318,港股中的09988,美股中的BABA等

所以，zvt里面投资标的的唯一编码(entity_id)为:{entity_type}\_{exchange}\_{code}

entity基类定义如下:
```
class EntityMixin(Mixin):
    entity_type = Column(String(length=64))
    exchange = Column(String(length=32))
    code = Column(String(length=64))
    name = Column(String(length=128))
```

### 1.2 投资标的发生的事

而投资标的发生的事，一定会有三个属性：
* **entity_id**

投资标的id

* **timestamp**

发生时间点(段)

* **id**

事件的唯一编码，一般使情况下格式为:{entity_id}_{timestamp}

entity发生的事情定义如下:
```
class Mixin(object):
    id = Column(String, primary_key=True)
    entity_id = Column(String)

    # the meaning could be different for different case,most of time it means 'happen time'
    timestamp = Column(DateTime)
```

>entity的诞生其实也是一个事件，这时，timestamp就代表其上市日。

## 2. 数据的稳定性和扩展性
稳定至少要达到以下的标准:
* **标准的字段**

不管数据来源何处，**确定的语义**在系统里面必须对应**确定的字段**；净资产收益率就叫roe,每股收益就叫eps,毛利率就叫gross_profit_margin。

* **完全分类(正交)**

技术面，基本面，宏观面，消息面等。

* **层次关系**

原始数据和衍生(计算)数据的关系，比如k线数据和各种技术指标；财报和各种财务指标。

而扩展性最重要的就是，**容易添加新数据**，并使得新数据无缝融入到系统中。

数据定义的目录为[domain](https://github.com/zvtvz/zvt/tree/master/zvt/domain)

## 3. 系统都有哪些数据？
```
In [1]: from zvt.domain import *
In [2]: global_schemas
[zvt.domain.dividend_financing.DividendFinancing,
 zvt.domain.dividend_financing.DividendDetail,
 zvt.domain.dividend_financing.SpoDetail...]
```

global_schemas就是系统支持的所有数据，具体含义可以查看相应字段的注释，或者调用相应schema的help方法:
```
In [3]: DividendFinancing.help()
class DividendFinancing(DividendFinancingBase, Mixin):
    __tablename__ = 'dividend_financing'

    provider = Column(String(length=32))
    code = Column(String(length=32))

    # 分红总额
    dividend_money = Column(Float)

    # 新股
    ipo_issues = Column(Float)
    ipo_raising_fund = Column(Float)

    # 增发
    spo_issues = Column(Float)
    spo_raising_fund = Column(Float)
    # 配股
    rights_issues = Column(Float)
    rights_raising_fund = Column(Float)
```

## 4. 如何查询数据？
查询数据，调用schema的query_data方法即可；由于该方法极为重要，有必要对其支持的参数进行详细的说明。

```
    @classmethod
    def query_data(cls,
                   provider_index: int = 0,
                   ids: List[str] = None,
                   entity_ids: List[str] = None,
                   entity_id: str = None,
                   codes: List[str] = None,
                   code: str = None,
                   level: Union[IntervalLevel, str] = None,
                   provider: str = None,
                   columns: List = None,
                   return_type: str = 'df',
                   start_timestamp: Union[pd.Timestamp, str] = None,
                   end_timestamp: Union[pd.Timestamp, str] = None,
                   filters: List = None,
                   session: Session = None,
                   order=None,
                   limit: int = None,
                   index: Union[str, list] = None,
                   time_field: str = 'timestamp'):
```
* provider_index

数据支持多provider,可以通过schema.providers来查看，provider_index为其providers的索引，默认为0

* ids

以id列表为过滤条件

* entity_ids

以entity_id列表为过滤条件

* entity_id

指定entity_id为过滤条件

* codes

以entity的code列表为过滤条件

* code

指定entity的code为过滤条件

* level

级别，对k线数据有用

* provider

指定provider,可以通过schema.providers来查看,默认不传，使用provider_index即可

* columns

查询返回的字段列表，类型为字符串或者schema.{column}列表,默认None,返回schema支持的所有字段

* return_type

目前支持df和domain,df为pandas dataframe格式，domain为数据库object,需要做数据库更新操作时使用。

* start_timestamp

开始时间过滤条件

* end_timestamp

结束时间过滤条件

* filters

其他的过滤条件列表，支持标准的[sql查询条件](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#common-filter-operators)

* session

操作schema的session,默认None,系统自动分配

* order

排序的方式，schema.{column}.asc()为升序，schema.{column}.desc()为降序

* limit

返回的数量限制，默认None,不限制

* index

返回df时，索引的字段

* time_field

代表时间的字段，默认为timestamp

### 4.1 一个查询例子

2019年年报 roe>8% 的前10个股

```
In [37]: from zvt.domain import * 
In [38]: df = FinanceProfitAbility.query_data(
    filters=[FinanceProfitAbility.roe_avg > 8,
             FinanceProfitAbility.report_period == 'year',
             ],
    start_timestamp='2019-01-01',
    limit=10,
    columns=FinanceProfitAbility.important_cols(),
    order=FinanceProfitAbility.roe_avg.desc())

In [5]:df
Out[5]: 
         entity_id    code  timestamp  gross_income_ratio  net_profit_ratio  roe_diluted    roe_avg   roe_wa  roe_ex_diluted  roe_ex_wa   net_roa       roa      roic
0  stock_sh_600186  600186 2019-12-31            10.15700          1.648130      22.2658  1104.1000      NaN       -84.23640        NaN   1.45342   4.41808  0.740165
1  stock_sz_000504  000504 2019-12-31            62.96810         13.617500     102.1310   460.7380 -1890.55      -153.46900    2848.07   5.97978   8.55756  0.148453
2  stock_sz_002175  002175 2019-12-31            24.45550         63.134100      89.6849   162.5980   162.60       -88.89860    -161.17  16.07950  21.68910  0.351641
3  stock_sh_600961  600961 2019-12-31             4.12899          0.844916     138.2840   145.1530      NaN       -97.32210        NaN   1.46388   4.15000  0.057221
4  stock_sz_002207  002207 2019-12-31            15.64960         17.176800      72.0933   114.0580   111.75         8.87405      13.76  11.82050  14.77190  0.409952
5  stock_sz_002458  002458 2019-12-31            65.37170         60.799100      60.4333    83.7598    83.18        60.41030      83.15  67.54280  67.60200  0.761227
6  stock_sz_002234  002234 2019-12-31            59.67640         49.127200      58.8250    83.4736    83.61        58.75640      83.51  54.69110  55.91570  0.656806
7  stock_sz_002629  002629 2019-12-31            20.45690         31.066100      55.8641    76.7945    76.79       -16.71070     -29.55   8.81773  10.58450  0.151190
8  stock_sz_300552  300552 2019-12-31            45.85380         25.996000      52.9783    72.5390    73.06        52.50790      72.42  40.81220  47.45930  0.683202
9  stock_sz_300116  300116 2019-12-31            12.11480         51.101700      52.2451    72.2721    77.64      -729.64200   -1084.31   2.94858   9.96187  0.197794
```

其他schema和查询条件使用方法是一样的，请自行探索。

## 5. 如何更新数据?

调用schema的record_data方法即可。

```
In [17]: FinanceFactor.provider_map_recorder
Out[17]: {'eastmoney': zvt.recorders.eastmoney.finance.china_stock_finance_factor_recorder.ChinaStockFinanceFactorRecorder}

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

定时任务的方式更新可参考[runners](https://github.com/zvtvz/zvt/blob/master/zvt/recorders/eastmoney/finance0_runner.py)