# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import FXRateKdataCommon

KdataBase = declarative_base()


class FXRate1dKdata(KdataBase, FXRateKdataCommon):
    __tablename__ = 'fxrate_1d_kdata'


register_schema(providers=['emquantapi'], db_name='fxrate_1d_kdata', schema_base=KdataBase)

__all__ = ['FXRate1dKdata']
