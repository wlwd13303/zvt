# -*- coding: utf-8 -*-
from zvt.domain import FinanceGrowthAbility
from zvt.recorders.emquantapi.finance.base_china_stock_finance_index_new import EmBaseChinaStockFinanceRecorder2
from zvt.utils.utils import add_func_to_value, first_item_to_float

financial_growth_ability_map = {
    # 总资产同比增长率（%）
    "asset_yoy":"YOYASSET",
    # 营业总收入同比增长率（%）
    "total_op_income_growth_yoy":"YOYGR",
    # 营业利润同比增长率（%）
    "op_yoy":"YOYOP" ,
    # 利润总额同比增长率（%）
    "ebt_yoy": "YOYEBT",
    # 净利润同比增长率（%）
    "ni_yoy": "YOYNI",
    # 归属母公司股东的净利润同比增长率（%）
    "inc_net_profit_shareholders_yoy": "YOYPNI",
    # 归属母公司股东的净利润同比增长率(扣非)（%）
    "deducted_net_profit_growth_yoy": "YOYPNIDEDUCTED",
    # 基本每股收益同比增长率（%）
    "basic_eps_you": "YOYEPSBASIC",
    # 稀释每股收益同比增长率（%）
    "diluted_eps_yoy": "YOYEPSDILUTED",
    # 净资产收益率同比增长率(摊薄)
    "roe_liluted_yoy": "YOYROELILUTED",
    # 经营活动产生的现金流量净额同比增长率（%）
    "cfo_yoy": "YOYCFO",
    # 每股经营活动中产生的现金流量净额同比增长率（%）
    "cfo_ps_yoy": "YOYCFOPS",
    # 资产总计相对年初增长率（%）
    "asset_relative": "ASSETRELATIVE",
    # 归属母公司股东的权益相对年初增长率（%）
    "equity_relative": "EQUITYRELATIVE",
    # 每股净资产相对年初增长率（%）
    "bps_relative": "BPSRELATIVE",
    # 营业收入环比增长率（%）
    'op_income_growth_qoq': 'RTROR',
    # 归属净利润滚动环比增长（%）
    'net_profit_growth_qoq': 'RTRNI',
    # 归属母公司股东的净利润环比增长率（扣非）（%）
    'deducted_net_profit_growth_qoq': 'RTRPNIDEDUCTED',
}

financial_growth_ability_map2 = {
    "op_profit_growth_yoy": "op_yoy",
    "net_profit_growth_yoy": "ni_yoy",
    "total_profit_growth_yoy": "ebt_yoy",
    "inc_net_profit_shareholders_deducted_yoy": "deducted_net_profit_growth_yoy",
    "net_op_cash_flows_yoy": "cfo_yoy",
    "net_operate_cash_flow_ps_yoy": "cfo_ps_yoy",
    "total_assets_relative_of_year": "asset_relative",
    "bps_relativeof_year": "bps_relative",
    "equity_relative_of_year": "equity_relative",
}

add_func_to_value(financial_growth_ability_map, first_item_to_float)


class ChinaStockFinanceGrowthAbilityRecorder(EmBaseChinaStockFinanceRecorder2):
    """
    财务指标-成长能力
    """
    data_schema = FinanceGrowthAbility

    finance_report_type = 'FinanceGrowthAbility'

    data_type = 5

    def get_data_map(self):
        return financial_growth_ability_map

    def get_data_map2(self):
        return financial_growth_ability_map2



__all__ = ['ChinaStockFinanceGrowthAbilityRecorder']

if __name__ == '__main__':
    # init_log('income_statement.log')
    recorder = ChinaStockFinanceGrowthAbilityRecorder(sleeping_time=0.1)
    recorder.run()
