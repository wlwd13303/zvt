# -*- coding: utf-8 -*-
from zvt.domain import FinanceIncomeStatementStructureAnalysis
from zvt.recorders.emquantapi.finance.base_china_stock_finance_recorder import EmBaseChinaStockFinanceRecorder
from zvt.utils.utils import add_func_to_value, first_item_to_float

finance_incomestatementstructureanalysis_map = {

    'financial_expense_rate': 'QFINAEXPENSETOGR',  # 财务费用与营业总收入之比
    'operating_profit_to_total_profit': 'QOPERATEINCOMETOEBT',  # 经营活动净收益与利润总额之比
    'net_profit_to_total_operate_revenue': 'QNITOGR',  # 净利润与营业总收入之比
    'admin_expense_rate': 'QADMINEXPENSETOGR',  # 管理费用与营业总收入之比
    'operating_profit_to_operating_revenue': 'QOPTOGR',  # 营业利润与营业总收入之比
    'total_operating_cost_to_total_operating_income': 'QGCTOGR',  # 营业总成本与营业总收入之比

}
add_func_to_value(finance_incomestatementstructureanalysis_map, first_item_to_float)


class ChinaStockFinanceIncomeStatementStructureAnalysisRecorder(EmBaseChinaStockFinanceRecorder):
    """
    财务指标-利润表结构分析
    """
    data_schema = FinanceIncomeStatementStructureAnalysis

    finance_report_type = 'FinanceIncomeStatementStructureAnalysis'

    data_type = 10

    def get_data_map(self):
        return finance_incomestatementstructureanalysis_map


__all__ = ['ChinaStockFinanceIncomeStatementStructureAnalysisRecorder']

if __name__ == '__main__':
    # init_log('income_statement.log')
    recorder = ChinaStockFinanceIncomeStatementStructureAnalysisRecorder(codes=['002572'])
    recorder.run()
