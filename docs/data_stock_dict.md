## 1. 个股估值表
|简称|英文简称|简介|数据类| |
|-----------|--------|--------|-----|-----|
|个股估值|stock_valuation|个股的估值类数据|StockValuation||
#### 个股估值表字段说明

|          字段          |                         含义                          |   单位   | 数据类型 | 数据示例 |
| :--------------------: | :---------------------------------------------------: | :----------: | ---- | ---- |
|           id           |                        索引id                         || str | stock_sh_600000_2005-01-04 |
|       entity_id        |                        数据id                         || str | stock_sh_600000 |
|       timestamp        |                       交易日期                        |      | datetime | 2005-01-04 00:00:00 |
|          code          |                       证券代码                        || str | 600000 |
|          name          |                       证券简称                        || str | 浦发银行 |
|     capitalization     |                      总股本                       |    股    | float | 3915000000 |
|    circulating_cap     |              流通股本               |    股    | float | 900000000 |
|       market_cap       |                         市值                          |  元  | float | 26935200000 |
| circulating_market_cap | 流通市值 |    元    | float | 6192000000 |
|     turnover_ratio     |                        换手率                         |    小数    | float | 0.004232 |
|           pe           |                        静态pe                         |    小数   | float | 17.199 |
|         pe_ttm         |                        动态pe                         |    小数   | float | 14.4219 |
|           pb           |                        市净率                         |    小数   | float | 2.0777 |
|           ps           |                        市销率                         |    小数   | float | 2.2097 |
|          pcf           |                        市现率                         |    小数   | float | 4.0393 |

##  2.财务指标-偿债能力表

| 简称              | 英文简称                   | 简介                                            | 数据类                   |      |
| ----------------- | -------------------------- | ----------------------------------------------- | ------------------------ | ---- |
| 财务指标-偿债能力 | finance_debtpaying_ability | 公司类型为通用的财务指标-偿债能力，支持沪深股票 | FinanceDebtpayingAbility |      |

#### 财务指标-偿债能力表字段说明

| 字段                                | 含义                                     | 单位 | 数据类型 | 数据示例                   |
| ----------------------------------- | ---------------------------------------- | ---- | -------- | -------------------------- |
| id                                  | 索引id                                   |      | str      | stock_sh_600004_2020-09-30 |
| entity_id                           | 数据id                                   |      | str      | stock_sh_600004            |
| timestamp                           | 报告日                                   |      | datetime | 2020-09-30 00:00:00        |
| provider                            | 数据源                                   |      | str      | emquantapi                 |
| code                                | 证券代码                                 |      | str      | 600004                     |
| report_period                       | 报告期                                   |      | str      | season3                    |
| report_date                         | 报告日                                   |      | datetime | 2020-09-30 00:00:00        |
| debt_asset_ratio                    | 资产负债率                               | %    | float    | 37.2325                    |
| conservative_quick_ratio            | 保守速动比率                             | 小数 | float    | 0.403392                   |
| equity_ratio                        | 产权比率                                 | 小数 | float    | 0.600506                   |
| equity_to_interest_libility         | 归属母公司股东的权益与带息债务之比       | 小数 | float    | 10.1666                    |
| equity_to_libility                  | 归属母公司股东的权益与负债合计之比       | 小数 | float    | 1.66526                    |
| cash_to_current_libility            | 货币资金与流动负债之比                   |      | float    | ？？？检查                 |
| cfo_to_interest_libility            | 经营活动产生的现金流量净额与带息债务之比 | 小数 | float    | 0.182659                   |
| cfo_to_libility                     | 经营活动产生的现金流量净额与负债合计之比 | 小数 | float    | 0.09374                    |
| cfo_to_net_libility                 | 经营活动产生的现金流量净额与净债务之比   | 小数 | float    | 0.2487                     |
| cfo_to_cl                           | 经营活动产生的现金流量净额与流动负债之比 | 小数 | float    | 0.1224                     |
| current_ratio                       | 流动比率                                 | 小数 | float    | 1.33968                    |
| quick_ratio                         | 速动比率                                 | 小数 | float    | 0.874608                   |
| ebitda_to_int_libility              | 息税折旧摊销前利润与带息债务之比         |      | float    | ？？？检查                 |
| ebitda_to_libility                  | 息税折旧摊销前利润与负债合计之比         | 小数 | float    | 0.191798                   |
| op_to_libility                      | 营业利润与负债合计之比                   |      | float    | ？？？检查                 |
| op_to_cl                            | 营业利润与流动负债之比                   |      | float    | ？？？检查                 |
| tangible_asset_to_interest_libility | 有形资产与带息债务之比                   | 小数 | float    | 4.29507                    |
| tangible_asset_to_libility          | 有形资产与负债合计之比                   | 小数 | float    | 2.3106                     |
| tangible_asset_to_net_libility      | 有形资产与净债务之比                     | 小数 | float    | 6.32703                    |