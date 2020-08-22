# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import StockKdataCommon

MoneyFlowBase = declarative_base()


class Stock1dMoneyflowKdata(MoneyFlowBase, StockKdataCommon):
    __tablename__ = 'stock_1d_money_flow'


register_schema(providers=['joinquant'], db_name='stock_1d_money_flow', schema_base=MoneyFlowBase)

__all__ = ['Stock1dMoneyflowKdata']
