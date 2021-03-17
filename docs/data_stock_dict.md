# ZvtData证券代码标准格式

由于同一代码可能代表不同的交易品种，ZvtData投资标的的唯一编码entity_id字段在所有表中进行定义，其构成为：{entity_type}_{exchange}_{code}以便于区分实际调用的交易品种。以下列出了每个交易市场的代码和示例代码。

#### 证券类型 entity_type

| entity_type | 含义     | 简介                     |      |
| ----------- | -------- | ------------------------ | ---- |
| index       | 指数     | 支持沪深市场指数         |      |
| stock       | 个股     | 支持沪深市场、港股、美股 |      |
| etf         | 场内基金 | 支持沪深市场             |      |
| fund        | 场外基金 | 支持沪深市场             |      |

#### 交易所 exchange

| exchange | 含义               | 简介 |
| -------- | ------------------ | ---- |
| sh       | 上海证券交易所     |      |
| sz       | 深圳证券交易所     |      |
| hk       | 香港证券交易所     |      |
| o        | 纳斯达克证券交易所 |      |
| a        | 美国证券交易所     |      |
| n        | 美国纽约证券交易所 |      |
|          |                    |      |


# 1 个股
## 1.1 个股基本资料

| 报表简称     | 英文简称 | 报表简介                                   | 数据类 |      |
| ------------ | -------- | ------------------------------------------ | ------ | ---- |
| 个股基本资料 | stock    | 个股简单基础数据，支持沪深股票、港股、美股 | Stock  |      |

#### 个股资料字段说明

| 字段        | 含义     | 数据类型 | 数据示例        |
| ----------- | -------- | -------- | --------------- |
| id          | 索引id   | str      | stock_sh_600000 |
| entity_id   | 数据id   | str      | stock_sh_600000 |
| timestamp   | 日期     | datetime | 1999-11-10      |
| entity_type | 数据类型 | str      | stock           |
| exchange    | 证券市场 | str      | sh              |
| code        | 证券代码 | str      | 600000          |
| name        | 证券简称 | str      | 浦发银行        |
| list_date   | 上市日   | datetime | 1999-11-10      |
| end_date    | 退市日   | datetime | 2200-01-01      |

​	

## 1.2 个股详细资料说明

| 报表简称     | 英文简称     | 报表简介                                  | 数据类      |      |
| ------------ | ------------ | ----------------------------------------- | ----------- | ---- |
| 个股详细资料 | stock_detail | 个股详细基础数据,支持沪深股票、港股、美股 | StockDetail |      |

#### 个股详细资料字段说明

| 字段                  | 含义       | 单位 | 数据类型 | 数据示例                                                     |
| --------------------- | ---------- | ---- | -------- | ------------------------------------------------------------ |
| id                    | 索引id     |      | str      | stock_sh_600000                                              |
| entity_id             | 数据id     |      | str      | stock_sh_600000                                              |
| timestamp             | 日期       |      | datetime | 1999-11-10                                                   |
| entity_type           | 数据类型   |      | str      | stock                                                        |
| exchange              | 证券市场   |      | str      | sh                                                           |
| code                  | 证券代码   |      | str      | 600000                                                       |
| name                  | 证券简称   |      | str      | 浦发银行                                                     |
| list_date             | 上市日     |      | datetime | 1999-11-10                                                   |
| end_date              | 退市日     |      | datetime | 2200-01-01(未退市以此时间填充)                               |
| industries            | 公司行业   |      | str      | 金融业、货币金融服务                                         |
| industry_indices      | 行业代码   |      | str      |                                                              |
| concept_indices       | 关联概念   |      | str      |                                                              |
| area_indices          | 关联地区   |      | str      | 上海                                                         |
| date_of_establishment | 成立日期   |      | datetime | 1992-10-19                                                   |
| profile               | 公司简介   |      | str      | 本行是经中国人民银行银复(1992)350号文批准，1992年10月由上海市财政局....... |
| main_business         | 主营业务   |      | str      | 金融与信托投资业务。                                         |
| issues                | 发行量     | 股   | int      | 320000000                                                    |
| price                 | 发行价格   | 元   | float    | 10                                                           |
| raising_fund          | 募资净额   | 元   | float    | 3200000000                                                   |
| issue_pe              | 发行市盈率 |      | float    |                                                              |
| net_winning_rate      | 网上中签率 |      | float    |                                                              |
| register_capital      | 注册资本   | 万元 | float    | 2935210                                                      |



## 1.3 个股行情表

| 简称     | 英文简称                                                     | 简介                                                         | 数据类 |      |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ | ---- |
| 个股行情 | stock_1d_kdata、（前复权）stock_1d_hfq_kdata、（后复权）stock_1d_bfq_kdata、（不复权）等 | 个股行情数据，支持日线，周线，月线级别，支持沪深股票，港股，美股 |        |      |

#### 数据类说明

| 数据类             | 含义         | 简介                     |      |
| ------------------ | ------------ | ------------------------ | ---- |
| Stock1dKdata       | 前复权、日线 | 支持沪深股票，港股，美股 |      |
| stock_1d_hfq_kdata | 后复权、日线 | 支持沪深股票，港股，美股 |      |
| stock_1d_bfq_kdata | 不复权、日线 | 支持沪深股票，港股，美股 |      |
| Stock1wkKdata      | 前复权、周线 | 支持沪深股票             |      |
| Stock1wkHfqKdata   | 后复权、周线 | 支持沪深股票             |      |
| Stock1wkBfqKdata   | 不复权、周线 | 支持沪深股票             |      |
| Stock1monKdata     | 前复权、月线 | 支持沪深股票             |      |
| Stock1monHfqKdata  | 后复权、月线 | 支持沪深股票             |      |
| Stock1monBfqKdata  | 不复权、月线 | 支持沪深股票             |      |



#### 个股行情表字段说明

|   字段    |   含义   | 单位 | 数据类型 | 数据示例                   |
| :-------: | :------: | :--: | -------- | -------------------------- |
|    id     |  索引id  |      | str      | stock_sh_600000_2005-01-04 |
| entity_id |  数据id  |      | str      | stock_sh_600000            |
| timestamp |   日期   |      | datetime | 2005-01-04                 |
| provider  |  数据源  |      | str      | joinquant                  |
|   code    | 证券代码 |      | str      | 600000                     |
|   name    | 证券简称 |      | str      | 浦发银行                   |
|   level   |   级别   |      | float    | 1d、1w、1m                 |
|   open    |  开盘价  |  元  | float    | 10.88                      |
|   close   |  收盘价  |  元  | float    | 11.12                      |
|   high    |  最高价  |  元  | float    | 11.24                      |
|    low    |  最低价  |  元  | float    | 10.88                      |
|  volume   |  成交量  |  手  | float    | 113524000                  |
| turnover  | 成交金额 |  元  | float    | 1259910000                 |
|           |          |      |          |                            |
|           |          |      |          |                            |

## 1.4 个股估值表

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

##  1.5 财务指标-偿债能力表

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

## 1.6 财务指标-成长能力表

| 简称                | 英文简称               | 简介                                            | 数据类               |      |
| ------------------- | ---------------------- | ----------------------------------------------- | -------------------- | ---- |
| 财务指标-成长能力表 | finance_growth_ability | 公司类型为通用的财务指标-成长能力，支持沪深股票 | FinanceGrowthAbility |      |

#### 财务指标-成长能力字段说明

| 字段                            | 含义                                       | 单位 | 数据类型 | 数据示例                   |
| ------------------------------- | ------------------------------------------ | ---- | -------- | -------------------------- |
| id                              | 索引id                                     |      | str      | stock_sh_600000_2020-09-30 |
| entity_id                       | 数据id                                     |      | str      | stock_sh_600000            |
| timestamp                       | 报告日                                     |      | datetime | 2020-09-30                 |
| provider                        | 数据源                                     |      | str      | emquantapi                 |
| code                            | 证券代码                                   |      | str      | 600000                     |
| report_period                   | 报告期                                     |      | str      | season3                    |
| report_date                     | 报告日                                     |      | datetime | 2020-09-30                 |
| pub_date                        | 更新日                                     |      | datetime | 2020-10-24                 |
| asset_yoy                       | 总资产同比增长率                           | %    | float    | 8.46                       |
| total_op_income_growth_yoy      | 营业总收入同比增长                         | %    | float    | 1.60                       |
| op_yoy                          | 营业利润同比增长率                         | %    | float    | -10.52                     |
| ebt_yoy                         | 利润总额同比增长率                         | %    | float    | 10.563                     |
| ni_yoy                          | 净利润同比增长率                           | %    | float    | -7.518                     |
| inc_net_profit_shareholders_yoy | 归属母公司股东的净利润同比增长率           | %    | float    | -7.462                     |
| deducted_net_profit_growth_yoy  | 扣非后归属母公司股东的净利润同比增长率     | %    | float    | 5.44212                    |
| basic_eps_you                   | 基本每股收益同比增长率                     | %    | float    | -10.91                     |
| diluted_eps_yoy                 | 稀释每股收益同比增长率                     | %    | float    | -10.91                     |
| roe_liluted_yoy                 | 净资产收益率同比增长率(摊薄)               | %    | float    | 12.77                      |
| cfo_yoy                         | 经营活动产生的现金流量净额同比增长率       | %    | float    | 411.48                     |
| cfo_ps_yoy                      | 每股经营活动中产生的现金流量净额同比增长率 | %    | float    | -249.03                    |
| asset_relative                  | 资产总计相对年初增长率                     | %    | float    | 1.37                       |
| equity_relative                 | 归属母公司股东的权益相对年初增长率         | %    | float    | 3.84                       |
| bps_relative                    | 每股净资产相对年初增长率                   | %    | float    | 20.1206                    |
| op_income_growth_qoq            | 营业收入环比增长率                         | %    | float    | 81.9664                    |
| net_profit_growth_qoq           | 归属净利润滚动环比增长                     | %    | float    | 77.4033                    |
| deducted_net_profit_growth_qoq  | 归属母公司股东的净利润环比增长率（扣非）   | %    | float    | 89.86                      |

## 1.7 财务指标-现金状况表

| 简称                | 英文简称              | 简介                                            | 数据类              |      |
| ------------------- | --------------------- | ----------------------------------------------- | ------------------- | ---- |
| 财务指标-现金状况表 | finance_cash_position | 公司类型为通用的财务指标-现金状况，支持沪深股票 | FinanceCashposition |      |

#### 财务指标-现金状况字段说明

| 字段                    | 含义                                       | 单位 | 数据类型 | 数据示例                   |
| ----------------------- | ------------------------------------------ | ---- | -------- | -------------------------- |
| id                      | 索引id                                     |      | str      | stock_sh_600000_2020-09-30 |
| entity_id               | 数据id                                     |      | str      | stock_sh_600000            |
| timestamp               | 报告日                                     |      | datetime | 2020-09-30                 |
| provider                | 数据源                                     |      | str      | emquantapi                 |
| code                    | 证券代码                                   |      | str      | 600000                     |
| report_period           | 报告期                                     |      | str      | season3                    |
| report_date             | 报告日                                     |      | datetime | 2020-09-30                 |
| pub_date                | 更新时间                                   |      | datetime | 2020-10-28                 |
| sales_cash_in_to_or     | 销售商品提供劳务收到的现金/营业收入        | %    | float    | 63.62                      |
| cfo_to_or               | 经营活动产生的现金流量净额/营业收入        | %    | float    | 1.27312                    |
| cfo_to_op_in            | 经营活动产生的现金流量净额/经营活动净收益  | %    | float    | 2.77255                    |
| capital_expenditure     | 资本支出/折旧摊销                          | %    | float    | 7.75521                    |
| sales_cash_in_to_or_ttm | 销售商品提供劳务收到的现金/营业收入（TTM） | %    | float    | 53.954                     |
| cfo_to_or_ttm           | 经营活动产生的现金流量净额/营业收入(TTM)   | %    | float    | -7.53                      |
| cfo_to_op_in_ttm        | 经营活动产生的现金流量净额/经营活动净收益  | %    | float    | 16.2768                    |
| cfo_to_gr               | 经营活动产生的现金流量净额/营业总收入      | %    | float    | 1.27312                    |
| cfo_to_np               | 经营活动产生的现金流量净额/净利润          | %    | float    | 3.74358                    |
|                         |                                            |      |          |                            |

## 1.8 财务指标-收益质量表

| 简称                | 英文简称                | 简介                                            | 数据类                |      |
| ------------------- | ----------------------- | ----------------------------------------------- | --------------------- | ---- |
| 财务指标-收益质量表 | finance_revenue_quality | 公司类型为通用的财务指标-收益质量，支持沪深股票 | FinanceRevenueQuality |      |

#### 财务指标-收益质量字段说明

| 字段                     | 含义                            | 单位 | 数据类型 | 数据示例                   |
| ------------------------ | ------------------------------- | ---- | -------- | -------------------------- |
| id                       | 索引id                          |      | str      | stock_sh_600000_2020-09-30 |
| entity_id                | 数据id                          |      | str      | stock_sh_600000            |
| timestamp                | 报告日                          |      | datetime | 2020-09-30                 |
| provider                 | 数据源                          |      | str      | emquantapi                 |
| code                     | 证券代码                        |      | str      | 600000                     |
| report_period            | 报告期                          |      | str      | season3                    |
| report_date              | 报告日                          |      | datetime | 2020-09-30                 |
| pub_date                 | 更新时间                        |      | datetime | 2020-10-28                 |
| non_op_profit            | 营业外收支净额                  | 元   | float    | 805653                     |
| invest_income_to_ebt     | 价值变动净收益/利润总额         | %    | float    | 33.266                     |
| non_op_profit_to_ebt     | 收支净额/利润总额               | %    | float    | 0.098528                   |
| tax_to_ebt               | 所得税/利润总额                 | %    | float    | 18.3585                    |
| deducted_profit_to_ebt   | 扣除非经常性损益的净利润/净利润 | %    | float    | 93.6218                    |
| op_income_to_ebt         | 经营活动净收益/利润总额         | %    | float    | 61.5585                    |
| op_income_to_ebt_ttm     | 经营活动净收益/利润总额(TTM)    | %    | float    | 66.0051                    |
| invest_income_to_ebt_ttm | 价值变动净收益/利润总额(TTM)    | %    | float    | 30.5702                    |
| non_op_profit_to_ebt_ttm | 营业外收支净额/利润总额(TTM)    | %    | float    | 0.006162                   |
|                          |                                 |      |          |                            |

## 1.9 财务指标-营运能力表

| 简称                | 英文简称                       | 简介                                            | 数据类                       |      |
| ------------------- | ------------------------------ | ----------------------------------------------- | ---------------------------- | ---- |
| 财务指标-营运能力表 | finance_operational_capability | 公司类型为通用的财务指标-营运能力，支持沪深股票 | FinanceOperationalCapability |      |

#### 财务指标-营运能力字段说明

| 字段                           | 含义                         | 单位  | 数据类型 | 数据示例                   |
| ------------------------------ | ---------------------------- | ----- | -------- | -------------------------- |
| id                             | 索引id                       |       | str      | stock_sh_600000_2020-09-30 |
| entity_id                      | 数据id                       |       | str      | stock_sh_600000            |
| timestamp                      | 报告日                       |       | datetime | 2020-09-30                 |
| provider                       | 数据源                       |       | str      | emquantapi                 |
| code                           | 证券代码                     |       | str      | 600000                     |
| report_period                  | 报告期                       |       | str      | season3                    |
| report_date                    | 报告日                       |       | datetime | 2020-09-30                 |
| pub_date                       | 更新时间                     |       | datetime | 2020-10-28                 |
| fixed_assets_turnover_rate     | 固定资产周转率               | 次    | float    | 0.66228                    |
| current_asset_turnover_rate    | 流动资产周转率               | 次    | float    | 0.197414                   |
| total_assets_turnover          | 总资产周转率                 | 次    | float    | 0.067888                   |
| inventory_turnover             | 存货周转率                   | 次    | float    | 0.067888                   |
| inventory_turnover_days        | 存货周转天数                 | 天/次 | float    | 0.067888                   |
| receivables_turnover           | 应收账款周转率(含应收票据)   | 次    | float    | 19.8445                    |
| receivables_turnover_days      | 应收账款周转天数(含应收票据) | 次    | float    | 13.6058                    |
| operating_cycle                | 营业周期                     | 天/次 | float    | 13.6058                    |
| accounts_payable_turnover_rate | 应付账款周转率               | 次    | float    | 13.6058                    |
| accounts_payable_turnover_days | 应付账款周转天数(含应付票据) | 天/次 | float    | 270.608                    |

## 1.10 财务指标-盈利能力表

| 简称                | 英文简称               | 简介                                            | 数据类               |      |
| ------------------- | ---------------------- | ----------------------------------------------- | -------------------- | ---- |
| 财务指标-盈利能力表 | finance_profit_ability | 公司类型为通用的财务指标-盈利能力，支持沪深股票 | FinanceProfitAbility |      |

#### 财务指标-盈利能力字段说明

| 字段                     | 含义                         | 单位 | 数据类型 | 数据示例                   |
| ------------------------ | ---------------------------- | ---- | -------- | -------------------------- |
| id                       | 索引id                       |      | str      | stock_sh_600000_2020-09-30 |
| entity_id                | 数据id                       |      | str      | stock_sh_600000            |
| timestamp                | 报告日                       |      | datetime | 2020-09-30                 |
| provider                 | 数据源                       |      | str      | emquantapi                 |
| code                     | 证券代码                     |      | str      | 600000                     |
| report_period            | 报告期                       |      | str      | season3                    |
| report_date              | 报告日                       |      | datetime | 2020-09-30                 |
| pub_date                 | 更新时间                     |      | datetime | 2020-10-28                 |
| gp_margin                | 销售毛利率                   | %    | float    | 57.2728                    |
| np_margin                | 销售净利率                   | %    | float    | 77.5744                    |
| roe_diluted              | 净资产收益率ROE(摊薄)        | %    | float    | 8.78991                    |
| roe_avg                  | 净资产收益率ROE(平均)        | %    | float    | 8.98326                    |
| roe_wa                   | 净资产收益率ROE(加权)        | %    | float    | 8.9                        |
| roe_ex_diluted           | 净资产收益率ROE(扣除/摊薄)   | %    | float    | 8.22927                    |
| roe_ex_wa                | 净资产收益率ROE(扣除/加权)   | %    | float    | 4.12                       |
| net_roa                  | 总资产净利率NROA             | %    | float    | 5.26637                    |
| roa                      | 总资产报酬率ROA              | %    | float    | 6.00195                    |
| roic                     | 投入资本回报率ROIC           | %    | float    | 0.053463                   |
| roe_ttm                  | 净资产收益率ROE(TTM)         | %    | float    | 71.25                      |
| roa_ttm                  | 总资产报酬率ROA(TTM)         | %    | float    | 71.25                      |
| n_roa_ttm                | 总资产净利率(TTM)            | %    | float    | -0.24                      |
| np_margin_ttm            | 销售净利率(TTM)              | %    | float    | 71.25                      |
| gp_margin_ttm            | 销售毛利率(TTM)              | %    | float    | 87.76                      |
| expense_to_ors_ttm       | 销售期间费用率(TTM)          | %    | float    | -0.24                      |
| ni_to_gr_ttm             | 净利润/营业总收入(TTM)       | %    | float    | 71.25                      |
| op_to_gr_ttm             | 营业利润/营业总收入(TTM)     | %    | float    | 87.76                      |
| gc_to_gr_ttm             | 营业总成本/营业总收入(TTM)   | %    | float    | 42.08                      |
| operae_expense_to_gr_ttm | 营业费用/营业总收入(TTM)     | %    | float    | 4.80                       |
| admin_expense_to_gr_ttm  | 管理费用/营业总收入(TTM)     | %    | float    | 4.80                       |
| fina_expense_to_gr_ttm   | 财务费用/营业总收入(TTM)     | %    | float    | -5.41                      |
| impart_to_gr_ttm         | 资产减值损失/营业总收入(TTM) | %    | float    | -5.41                      |
| deducted_roe_ttm         | 净资产收益率ROETTM(扣非)     | %    | float    | 11.97                      |
| roic_ttm                 | 投入资本回报率ROIC(TTM)      | %    | float    | 5.78                       |
| np_to_cost_expense       | 成本费用利润率               | %    | float    | 231.80                     |
| rd_expense_to_gr         | 研发费用/营业总收入          | %    | float    | 57.27                      |

## 1.11 财务指标-资本结构表

| 简称                | 英文简称                 | 简介                                            | 数据类                  |      |
| ------------------- | ------------------------ | ----------------------------------------------- | ----------------------- | ---- |
| 财务指标-资本结构表 | finace_capital_structure | 公司类型为通用的财务指标-资本结构，支持沪深股票 | FinanceCapitalStructure |      |

#### 财务指标-资本结构字段说明

| 字段                              | 含义     | 单位 | 数据类型 | 数据示例                   |
| --------------------------------- | -------- | ---- | -------- | -------------------------- |
| id                                | 索引id   |      | str      | stock_sh_600000_2020-09-30 |
| entity_id                         | 数据id   |      | str      | stock_sh_600000            |
| timestamp                         | 报告日   |      | datetime | 2020-09-30                 |
| provider                          | 数据源   |      | str      | emquantapi                 |
| code                              | 证券代码 |      | str      | 600000                     |
| report_period                     | 报告期   |      | str      | season3                    |
| report_date                       | 报告日   |      | datetime | 2020-09-30                 |
| pub_date                          | 更新时间 |      | datetime | 2020-10-28                |
| debt_asset_ratio                  | 资产负债率 | % | float | 36.6635 |
| em                                | 权益乘数 | % | float | 1.57887 |
| ca_to_asset                       | 流动资产/总资产 | % | float | 38.7697 |
| nc_to_asset                       | 非流动资产/总资产 | % | float | 61.2303 |
| tangible_assets_to_asset          | 有形资产/总资产 | % | float | 43.4084 |
| equity_to_total_capital           | 归属母公司股东的权益/全部投入资本 | % | float | 61.3199 |
| interest_liblity_to_total_capital | 带息负债/全部投入资本 | % | float | 33.1622 |
| cl_to_libility      | 流动负债/负债合计                 | % | float | 54.6746 |
| cnl_to_libility                   | 非流动负债/负债合计 | % | float | 45.3254 |
| interest_liblity_to_libility      | 有息负债率 | % | float | 75.5413 |
|                                   |          |      |          ||

## 1.12 财务指标-杜邦分析表

| 简称                | 英文简称        | 简介                                            | 数据类        |      |
| ------------------- | --------------- | ----------------------------------------------- | ------------- | ---- |
| 财务指标-杜邦分析表 | finance_du_pont | 公司类型为通用的财务指标-杜邦分析，支持沪深股票 | FinanceDuPont |      |

#### 财务指标-杜邦分析字段说明

| 字段                                      | 含义                          | 单位 | 数据类型 | 数据示例                   |
| ----------------------------------------- | ----------------------------- | ---- | -------- | -------------------------- |
| id                                        | 索引id                        |      | str      | stock_sh_600000_2020-09-30 |
| entity_id                                 | 数据id                        |      | str      | stock_sh_600000            |
| timestamp                                 | 报告日                        |      | datetime | 2020-09-30                 |
| provider                                  | 数据源                        |      | str      | emquantapi                 |
| code                                      | 证券代码                      |      | str      | 600000                     |
| report_period                             | 报告期                        |      | str      | season3                    |
| report_date                               | 报告日                        |      | datetime | 2020-09-30                 |
| pub_date                                  | 更新时间                      |      | datetime | 2020-10-28                 |
| inc_net_profit_shareholders_to_net_profit | 归属母公司股东的净利润/净利润 | %    | float    | 99.6025                    |
| roe_avg                                   | 净资产收益率ROE               | %    | float    | 8.98326                    |
| em                                        | 权益乘数(杜邦分析)            | %    | float    | 1.71259                    |
| total_assets_turnover                     | 总资产周转率                  | 次   | float    | 0.067888                   |
| net_profit_to_total_operate_revenue       | 净利润/营业总收入             | %    | float    | 77.5744                    |
| net_profit_to_total_profits               | 净利润/利润总额               | %    | float    | 81.6415                    |
| total_profits_to_fi_ebit                  | 利润总额/息税前利润           | %    | float    | 107.475                    |
| fi_ebit_to_total_op_income                | 息税前利润/营业总收入         | %    | float    | 88.4096                    |
|                                           |                               |      |          |                            |

# 2 指数

## 2.1 指数基础资料

| 报表简称     | 英文简称 | 报表简介                         | 数据类 |      |
| ------------ | -------- | -------------------------------- | ------ | ---- |
| 指数基础资料 | index    | 指数的简单基础数据，支持沪深市场 | Index  |      |

#### 指数基础资料字段说明

|    字段     |   含义   | 数据类型 | 数据示例        |
| :---------: | :------: | -------- | --------------- |
|     id      |  索引id  | str      | index_sh_000001 |
|  entity_id  |  数据id  | str      | index_sh_000001 |
|  timestamp  |   日期   | datetime | 1991-07-15      |
| entity_type | 数据类型 | str      | index           |
|  exchange   | 证券市场 | str      | sh              |
|    code     | 指数代码 | str      | 000001          |
|    name     | 指数名称 | str      | 上证指数        |
|  list_date  |  上市日  | datetime | 1991-07-15      |
|  end_date   |  退市日  | datetime |                 |
|  publisher  |  发布商  | str      | 上海证券交易所  |
|  category   |   类别   | str      | main            |
| base_point  | 基准点数 | float    | 100             |

## 2.1 指数行情

| 报表简称 | 英文简称                                       | 报表简介                                             | 数据类 |      |
| -------- | ---------------------------------------------- | ---------------------------------------------------- | ------ | ---- |
| 指数行情 | index_1d_kdata、index_1w_kdata、index_1m_kdata | 指数行情数据，支持日线，周线，月线级别，支持沪深市场 |        |      |

#### 数据类说明

| 数据类         | 含义 | 简介         |      |
| -------------- | ---- | ------------ | ---- |
| Index1dKdata   | 日线 | 支持沪深股票 |      |
| Index1wkKdata  | 周线 | 支持沪深股票 |      |
| Index1monKdata | 月线 | 支持沪深股票 |      |
|                |      |              |      |

#### 指数行情字段说明

|   字段    |   含义   | 单位 | 数据类型 | 数据示例                   |
| :-------: | :------: | :--: | -------- | -------------------------- |
|    id     |  索引id  |      | str      | index_sh_000001_2021-03-16 |
| entity_id |  数据id  |      | str      | index_sh_000001            |
| timestamp |   日期   |      | datetime | 2021-03-16                 |
| provider  |  数据源  |      | str      | joinquant                  |
|   code    | 证券代码 |      | str      | 600000                     |
|   name    | 证券简称 |      | str      | 上证指数                   |
|   level   |   级别   |      | float    | 1d、1w、1m                 |
|   open    |  开盘价  |  元  | float    | 3424.65                    |
|   close   |  收盘价  |  元  | float    | 3446.73                    |
|   high    |  最高价  |  元  | float    | 3448.88                    |
|    low    |  最低价  |  元  | float    | 3406.17                    |
|  volume   |  成交量  |  手  | float    | 31666900000                |
| turnover  | 成交金额 |  元  | float    | 332388000000               |
|           |          |      |          |                            |
|           |          |      |          |                            |