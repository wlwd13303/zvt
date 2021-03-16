# -*- coding: utf-8 -*-
from zvt.domain import FinancePerShare
from zvt.recorders.emquantapi.finance.base_china_stock_finance_index import EmBaseChinaStockFinanceIndexRecorder
from zvt.utils.utils import add_func_to_value, first_item_to_float

finance_per_share_map = {
    "fcfe_ps": "FCFEPS",  # 每股股东自由现金流量
    "fcff_ps": "FCFFPS",  # 每股企业自由现金流量
    "cf_ps_ttm": "CFPSTTM",  # 每股现金流量净额TTM(元)
    "cf_ps": "CFPS",  # 每股现金流量净额(元)
    "cfo_ps_ttm": "CFOPSTTM",  # 每股经营活动产生的现金流量净额TTM(元)
    "cfo_ps": "CFOPS",  # 每股经营活动产生的现金流量净额(元)
    "retained_ps": "RETAINEDPS",  # 每股留存收益(元)
    "undistributed_ps": "UNDISTRIBUTEDPS",  # 每股未分配利润(元)
    "surplus_reserve_ps": "SURPLUSRESERVEPS",  # 每股盈余公积(元)
    "capital_reserve_ps": "CAPITALRESERVEPS",  # 每股资本公积(元)
    "ebit_ps": "EBITPS",  # 每股息税前利润(元)
    "or_ps_ttm": "ORPSTTM",  # 每股营业收入TTM(元)
    "or_ps": "ORPS",  # 每股营业收入(元)
    "gr_ps": "GRPS",  # 每股营业总收入(元)
    "bps": "BPS",  # 每股净资产(元)
    "eps_ttm": "EPSTTM",  # 每股收益EPSTTM(元)
    "deducted_eps": "EPSEXBASIC",  # 扣非每股收益(元)
    "diluted_eps": "EPSDILUTED",  # 稀释每股收益(元)
    "eps_diluted_end": "EPSDILUTEDEND",  # 期末摊薄每股收益(元)
    "eps": "EPSBASIC",  # 基本每股收益(元)
}

add_func_to_value(finance_per_share_map, first_item_to_float)


class ChinaStockFinancePerShareRecorder(EmBaseChinaStockFinanceIndexRecorder):
    data_schema = FinancePerShare

    finance_report_type = 'FinancePerShare'

    data_type = 7

    def get_data_map(self):
        return finance_per_share_map


__all__ = ['ChinaStockFinancePerShareRecorder']

if __name__ == '__main__':
    # init_log('income_statement.log')
    recorder = ChinaStockFinancePerShareRecorder(codes=['002572'])
    recorder.run()
