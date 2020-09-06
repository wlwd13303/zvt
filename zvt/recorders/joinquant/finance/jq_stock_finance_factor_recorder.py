# -*- coding: utf-8 -*-
from zvt.utils.time_utils import to_pd_timestamp
from zvt.utils.utils import add_func_to_value, to_float
from zvt.api.quote import to_report_period_type
from zvt.domain import FinanceFactor
from zvt.recorders.joinquant.finance.base_jq_stock_finance_recorder import BaseJqStockFinanceRecorder

finance_factor_map = {

    # 基本每股收益(元)
    "basic_eps": "eps",
    # 扣非每股收益(元)
    "deducted_eps": "adjusted_profit",
    # 稀释每股收益(元)
    "diluted_eps": "diluted_eps",
    # 每股净资产(元)
    "bps": "net_asset_per_share",
    # 每股资本公积(元)
    "capital_reserve_ps": "capital_reserve_fund_per_share",
    # 每股未分配利润(元)
    ###"undistributed_profit_ps": "retained_profit_per_share",
    # 每股经营现金流(元)
    ###"op_cash_flow_ps": "cashflow_per_share_ttm",
    # 成长能力指标
    #
    # 营业总收入(元)
    # "total_op_income": "total_operating_revenue",
    # 毛利润(元)
    ### "gross_profit": "Grossprofit",
    # 净利润(元)
    # "net_profit": "net_profit",
    # 归属于母公司所有者的净利润(元)
    "np_parent_company_owners": "np_parent_company_owners",
    # 扣除非经常损益后的净利润(元)
    "deducted_net_profit": "adjusted_profit",
    # 营业总收入同比增长率
    "op_income_growth_yoy": "inc_total_revenue_year_on_year",
    # 归属母公司股东的净利润同比增长率
    "net_profit_growth_yoy ": "inc_net_profit_to_shareholders_year_on_year",
    # 扣非净利润同比增长
    ###"deducted_net_profit_growth_yoy": "Bucklenetprofityoy",
    # 营业总收入滚动环比增长
    "op_income_growth_qoq": "inc_total_revenue_annual",
    # 归属净利润滚动环比增长
    "net_profit_growth_qoq": "inc_net_profit_to_shareholders_annual",
    # 扣非净利润滚动环比增长
    ###"deducted_net_profit_growth_qoq": "Bucklenetprofitrelativeratio",
    # 盈利能力指标
    #
    # 净资产收益率(加权)
    "roe": "roe",
    # 净资产收益率(扣非/加权)
    "deducted_roe": "inc_return",
    # 总资产收益率(加权)
    ###"rota": "Allcapitalearningsrate",
    # 毛利率
    "gross_profit_margin": "gross_profit_margin",
    # 净利率
    "net_margin": "net_profit_margin",
    # 收益质量指标
    #
    # 预收账款/营业收入
    ###"advance_receipts_per_op_income": "Accountsrate",
    # 销售净现金流/营业收入
    ###"sales_net_cash_flow_per_op_income": "Salesrate",
    # 经营净现金流/营业收入
    ###"op_net_cash_flow_per_op_income": "Operatingrate",
    # 实际税率
    ###"actual_tax_rate": "Taxrate",
    # 财务风险指标
    #
    # 流动比率
    ###"current_ratio": "Liquidityratio",
    # 速动比率
    ###"quick_ratio": "Quickratio",
    # 现金流量比率
   ### "cash_flow_ratio": "Cashflowratio",
    # 资产负债率
    ###"debt_asset_ratio": "Assetliabilityratio",
    # 权益乘数
    ###"em": "Equitymultiplier",
    # 产权比率
    ###"equity_ratio": "Equityratio",
    # 营运能力指标(一般企业)
    #
    # 总资产周转天数(天)
    ###"total_assets_turnover_days": "Totalassetsdays",
    # 存货周转天数(天)
    "inventory_turnover_days": "Inventorydays",
    # 应收账款周转天数(天)
    "receivables_turnover_days": "Accountsreceivabledays",
    # 总资产周转率(次)
    "total_assets_turnover": "Totalassetrate",
    # 存货周转率(次)
    "inventory_turnover": "Inventoryrate",
    # 应收账款周转率(次)
    "receivables_turnover": "Accountsreceiveablerate",

    # 专项指标(银行)
    #
    # 存款总额
    "fi_total_deposit": "Totaldeposit",
    # 贷款总额
    "fi_total_loan": "Totalloan",
    # 存贷款比例
    "fi_loan_deposit_ratio": "Depositloanratio",
    # 资本充足率
    "fi_capital_adequacy_ratio": "Capitaladequacyratio",
    # 核心资本充足率
    "fi_core_capital_adequacy_ratio": "Corecapitaladequacyratio",
    # 不良贷款率
    "fi_npl_ratio": "Nplratio",
    # 不良贷款拨备覆盖率
    "fi_npl_provision_coverage": "Nplprovisioncoverage",
    # 资本净额
    "fi_net_capital": "Netcapital_b",
    # 专项指标(保险)
    #
    # 总投资收益率
    "insurance_roi": "Tror",
    # 净投资收益率
    "insurance_net_investment_yield": "Nror",
    # 已赚保费
    "insurance_earned_premium": "Eapre",
    # 赔付支出
    "insurance_payout": "Comexpend",
    # 退保率
    "insurance_surrender_rate": "Surrate",
    # 偿付能力充足率
    "insurance_solvency_adequacy_ratio": "Solvenra",
    # 专项指标(券商)
    #
    # 净资本
    "broker_net_capital": "Netcapital",
    # 净资产
    "broker_net_assets": "Netassets",
    # 净资本/净资产
    "broker_net_capital_assets_ratio": "Captialrate",
    # 自营固定收益类证券规模/净资本
    "broker_self_operated_fixed_income_securities_net_capital_ratio": "Incomesizerate",
}

add_func_to_value(finance_factor_map, to_float)
finance_factor_map["report_period"] = ("ReportDate", to_report_period_type)
finance_factor_map["report_date"] = ("ReportDate", to_pd_timestamp)


class JqStockFinanceFactorRecorder(BaseJqStockFinanceRecorder):
    finance_report_type = 'ZhuYaoZhiBiaoList'

    data_schema = FinanceFactor
    data_type = 1

    def get_data_map(self):
        return finance_factor_map


__all__ = ['JqStockFinanceFactorRecorder']

if __name__ == '__main__':
    # init_log('finance_factor.log')
    recorder = JqStockFinanceFactorRecorder(codes=['000001'])
    recorder.run()