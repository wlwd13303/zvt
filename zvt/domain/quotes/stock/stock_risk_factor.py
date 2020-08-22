# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import StockRiskFactorCommon

FactorBase = declarative_base()


class StockRiskFactor(FactorBase, StockRiskFactorCommon):
    @classmethod
    def important_cols(cls):
        return [
                'Kurtosis120', 'Kurtosis20',
                'Kurtosis60', 'sharpe_ratio_120', 'sharpe_ratio_20',
                'sharpe_ratio_60', 'Skewness120', 'Skewness20', 'Skewness60',
                'Variance120', 'Variance20', 'Variance60']

    __tablename__ = 'stock_risk_factor'


register_schema(providers=['joinquant'], db_name='stock_risk_factor', schema_base=FactorBase)

__all__ = ['StockRiskFactor']