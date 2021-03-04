[![image](https://img.shields.io/pypi/v/zvt.svg)](https://pypi.org/project/zvt/)
[![image](https://img.shields.io/pypi/l/zvt.svg)](https://pypi.org/project/zvt/)
[![image](https://img.shields.io/pypi/pyversions/zvt.svg)](https://pypi.org/project/zvt/)
[![Build Status](https://api.travis-ci.org/zvtvz/zvt.svg?branch=master)](https://travis-ci.org/zvtvz/zvt)
[![codecov.io](https://codecov.io/github/zvtvz/zvt/coverage.svg?branch=master)](https://codecov.io/github/zvtvz/zvt)
[![HitCount](http://hits.dwyl.io/zvtvz/zvt.svg)](http://hits.dwyl.io/zvtvz/zvt)

ZVTData是在zvt的基础上编写的量化数据服务，其包含沪深股票、港股和美股的历史行情和财务数据。

编写该系统的初心:
* 构造一个中立标准的数据schema
* 能够容易地把各provider的数据适配到系统
* 相同的算法，只写一次，可以应用到任何市场

## ✨产品与服务综览
- **股票，ETF，汇率，债券数据服务：数据库格式（MySQL）**
    - 海外股票数据：
        - 港股数据：包括港股财务数据（实现中）、港股GICS行业分类数据(实现中）
        - 美股数据：包括美股财务数据（实现中）、美股GICS行业分类数据(实现中）
        - 港股、美股股票的历史数据及每日数据服务。历史数据可提供日线数据、周线数据及月线数据。 包括了美国证交所（AMEX）、美国纳斯达克市场（Nasdaq，同时包含NasdaqNM及NasdaqSC）、纽约证券交易所（NYSE）、香港联交所（主板、创业板）等市场的股票历史数据。
    - 沪深市场:
        - 提供沪深市场的权息数据及财务数据：包括公司历年募资、分红派息配股送股等权息记录，以及股本结构和股权状况。上市公司和债券发行人披露的财务报表、财务附注、重要财务指标等。
        - 沪深市场的历史数据及每日数据服务。历史数据可提供日线数据、周线数据及月线数据。
        - 沪深市场的指数数据、债券数据以及宏观经济数据（实现中）
- 数据的标准化,多数据源(provider)交叉验证,补全
- **简洁可扩展的数据框架**
- **统一简洁的API,支持sql查询,支持pandas**

## 💯关于该文档

该文档由[项目docs]

------