# -*- coding: utf-8 -*-
from zvt.domain import FinanceProfitAbility
from zvt.recorders.emquantapi.finance.base_china_stock_finance_index_new import EmBaseChinaStockFinanceRecorder2
from zvt.utils.utils import add_func_to_value, first_item_to_float

financial_profitability_map = {

    'gp_margin': 'GPMARGIN',  # 销售毛利率
    'np_margin': 'NPMARGIN',  # 销售净利率

    'roe_diluted': 'ROEDILUTED',  # 净资产收益率ROE(摊薄)
    'roe_avg': 'ROEAVG',  # 净资产收益率ROE(平均)
    'roe_wa': 'ROEWA',  # 净资产收益率ROE(加权)
    'roe_ex_diluted': 'ROEEXDILUTED',  # 净资产收益率ROE(扣除/摊薄)
    'roe_ex_wa': 'ROEEXWA',  # 净资产收益率ROE(扣除/加权)

    'net_roa': 'NROA',  # 总资产净利率ROA
    'roa': 'ROA',  # 总资产报酬率ROA
    'roic': 'ROIC',  # 投入资本回报率ROIC
            
    'roe_ttm': 'ROETTM',  # 净资产收益率ROE(TTM)
    'roa_ttm': 'ROATTM',  # 总资产报酬率ROA(TTM)
    'n_roa_ttm': 'NROATTM',  # 总资产净利率(TTM)
    'np_margin_ttm': 'NPMARGINTTM',  # 销售净利率(TTM)
    'gp_margin_ttm': 'GPMARGINTTM',  # 销售毛利率(TTM)
    'expense_to_ors_ttm': 'EXPENSETOORSTTM',  # 销售期间费用率(TTM)
    'ni_to_gr_ttm': 'NITOGRTTM',  # 净利润/营业总收入(TTM)
    'op_to_gr_ttm': 'OPTOGRTTM',  # 营业利润/营业总收入(TTM)
    'gc_to_gr_ttm': 'GCTOGRTTM',  # 营业总成本/营业总收入(TTM)
    'operae_expense_to_gr_ttm': 'OPERATEEXPENSETOGRTTM',  # 营业费用/营业总收入(TTM)
    'admin_expense_to_gr_ttm': 'ADMINEXPENSETOGRTTM',  # 管理费用/营业总收入(TTM)
    'fina_expense_to_gr_ttm': 'FINAEXPENSETOGRTTM',  # 财务费用/营业总收入(TTM)
    'impart_to_gr_ttm': 'IMPAIRTOGRTTM',  # 资产减值损失/营业总收入(TTM)
    'deducted_roe_ttm': 'ROETTMDEDUCTED',  # 净资产收益率ROETTM(扣非)
    'roic_ttm': 'ROICTTM',  # 投入资本回报率ROIC(TTM)
    'np_to_cost_expense': 'NPTOCOSTEXPENSE',  # 成本费用利润率
    'rd_expense_to_gr': 'RDEXPENSETOGR',  # 研发费用/营业总收入
}
financial_profitability_map2 = {

}

add_func_to_value(financial_profitability_map, first_item_to_float)


class ChinaStockFinanceProfitAbilityRecorder(EmBaseChinaStockFinanceRecorder2):
    """
    财务指标-盈利能力
    """
    data_schema = FinanceProfitAbility

    finance_report_type = 'FinanceProfitAbility'

    data_type = 8

    def get_data_map(self):
        return financial_profitability_map

    def get_data_map2(self):
        return financial_profitability_map2

__all__ = ['ChinaStockFinanceProfitAbilityRecorder']

if __name__ == '__main__':
    # init_log('income_statement.log')
    recorder = ChinaStockFinanceProfitAbilityRecorder(exchanges=['sh'],sleeping_time=0.1)
    recorder.run()
