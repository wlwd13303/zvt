# -*- coding: utf-8 -*-
from zvt.domain import FinanceCashposition
from zvt.recorders.emquantapi.finance.base_china_stock_finance_index import EmBaseChinaStockFinanceIndexRecorder
from zvt.utils.utils import add_func_to_value, first_item_to_float

financial_debtpayingability_map = {
    # 销售商品提供劳务收到的现金/营业收入
    'sales_cash_in_to_or': 'SALESCASHINTOOR',

    # 经营活动产生的现金流量净额/营业收入
    'cfo_to_or': 'CFOTOOR',
    # 经营活动产生的现金流量净额/经营活动净收益
    'cfo_to_op_in': 'CFOTOOPERATEINCOME',
    # 资本支出/折旧摊销
    'capital_expenditure':"CAPITALEXPENDITURE",
    # 销售商品提供劳务收到的现金/营业收入 ttm
    'sales_cash_in_to_or_ttm': 'SALESCASHINTOORTTM',
    # 经营活动产生的现金流量净额/营业收入 ttm
    'cfo_to_or_ttm': 'CFOTOORTTM',

    # 经营活动产生的现金流量净额/经营活动净收益
    'cfo_to_op_in_ttm': 'CFOTOOPERATEINCOMETTM',

    # 经营活动产生的现金流量净额/营业总收入
    'cfo_to_gr': 'CFOTOGR',
    # 经营活动产生的现金流量净额/净利润
    'cfo_to_np': 'CFOTONP',

}
add_func_to_value(financial_debtpayingability_map, first_item_to_float)


class ChinaStockFinanceCashpositionRecorder(EmBaseChinaStockFinanceIndexRecorder):
    """
    财务指标-收现能力
    """
    data_schema = FinanceCashposition
    finance_report_type = 'FinanceReceivingAbility'
    data_type = 9
    def get_data_map(self):
        return financial_debtpayingability_map


__all__ = ['ChinaStockFinanceCashpositionRecorder']

if __name__ == '__main__':
    # init_log('income_statement.log')
    recorder = ChinaStockFinanceCashpositionRecorder(sleeping_time=0.1)
    recorder.run()
