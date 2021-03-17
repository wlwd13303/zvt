# -*- coding: utf-8 -*-
from zvt.domain import FinanceRevenueQuality
from zvt.recorders.emquantapi.finance.base_china_stock_finance_index import EmBaseChinaStockFinanceIndexRecorder
from zvt.utils.utils import add_func_to_value, first_item_to_float

# 财务指标-收益质量
finance_qualityofearnings_map = {
    # 营业外收支净额
    "non_op_profit": "NONOPERATEPROFIT",
    # 价值变动净收益/利润总额
    "invest_income_to_ebt": "INVESTINCOMETOEBT",
    # 营业外收支净额/利润总额
    "non_op_profit_to_ebt": "NONOPERATEPROFITTOEBT",
    # 所得税/利润总额
    "tax_to_ebt": "TAXTOEBT",
    # 扣除非经常性损益的净利润/净利润
    "deducted_profit_to_ebt": "DEDUCTEDPROFITTOEBT",
    # 经营活动净收益/利润总额
    "op_income_to_ebt": "OPERATEINCOMETOEBT",
    # 经营活动净收益/利润总额(TTM)
    "op_income_to_ebt_ttm": "OPERATEINCOMETOEBTTTM",
    # 价值变动净收益/利润总额(TTM)
    "invest_income_to_ebt_ttm": "INVESTINCOMETOEBTTTM",
    # 营业外收支净额/利润总额(TTM)
    "non_op_profit_to_ebt_ttm": "NONOPERATEPROFITTOEBTTTM",
}

add_func_to_value(finance_qualityofearnings_map, first_item_to_float)


class ChinaStockFinanceRevenueQualityRecorder(EmBaseChinaStockFinanceIndexRecorder):
    """
    财务指标-收益质量
    """
    data_schema = FinanceRevenueQuality

    finance_report_type = 'FinanceRevenueQuality'

    data_type = 8

    def get_data_map(self):
        return finance_qualityofearnings_map


__all__ = ['ChinaStockFinanceRevenueQualityRecorder']

if __name__ == '__main__':
    # init_log('income_statement.log')
    recorder = ChinaStockFinanceRevenueQualityRecorder(exchanges=['sh'],sleeping_time=0.1)
    recorder.run()
