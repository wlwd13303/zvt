# -*- coding: utf-8 -*-
import pandas as pd
from zvt.recorders.joinquant.common import JoinquantTimestampsDataRecorder, call_joinquant_api, get_from_path_fields, \
    get_fc
from zvt.api import to_report_period_type
from zvt.contract.api import df_to_db, get_data
from zvt.domain import StockDetail, FinancePerShare, BalanceSheet
from zvt.recorders.emquantapi.common import mainCallback, to_em_entity_id
from zvt.utils.pd_utils import pd_is_not_null
from zvt.utils.time_utils import to_time_str, TIME_FORMAT_DAY, now_pd_timestamp, to_pd_timestamp

try:
    from EmQuantAPI import c
except:
    pass


class EmBaseChinaStockFinanceRecorder2(JoinquantTimestampsDataRecorder):
    finance_report_type = None
    data_type = 1

    timestamps_fetching_url = 'https://emh5.eastmoney.com/api/CaiWuFenXi/GetCompanyReportDateList'
    timestamp_list_path_fields = ['CompanyReportDateList']
    timestamp_path_fields = ['ReportDate']

    entity_provider = 'joinquant'
    entity_schema = StockDetail
    provider = 'emquantapi'

    def __init__(self, entity_type='stock', exchanges=['sh', 'sz'], entity_ids=None, codes=None, batch_size=10,
                 force_update=False, sleeping_time=5, default_size=2000, real_time=False,
                 fix_duplicate_way='add', start_timestamp=None, end_timestamp=None, close_hour=0,
                 close_minute=0) -> None:
        super().__init__(entity_type, exchanges, entity_ids, codes, batch_size, force_update, sleeping_time,
                         default_size, real_time, fix_duplicate_way, start_timestamp, end_timestamp, close_hour,
                         close_minute)

        # 调用登录函数（激活后使用，不需要用户名密码）
        loginResult = c.start("ForceLogin=1", '', mainCallback)
        if (loginResult.ErrorCode != 0):
            print("login in fail")
            exit()

    def on_finish(self):
        # 退出
        loginresult = c.stop()
        if (loginresult.ErrorCode != 0):
            print("login in fail")
            exit()

    def init_timestamps(self, entity):
        param = {
            "color": "w",
            "fc": get_fc(entity),
            "DataType": 1
        }

        if self.finance_report_type == 'INCOME_STATEMENT' or self.finance_report_type == 'CASHFLOW_STATEMENT':
            param['ReportType'] = 1

        timestamp_json_list = call_joinquant_api(url=self.timestamps_fetching_url,
                                                 path_fields=self.timestamp_list_path_fields,
                                                 param=param)

        if self.timestamp_path_fields:
            timestamps = [get_from_path_fields(data, self.timestamp_path_fields) for data in timestamp_json_list]

        return [to_pd_timestamp(t) for t in timestamps]

    def generate_request_param(self, security_item, start, end, size, timestamps):
        return [to_time_str(i) for i in (timestamps)]

    def record(self, entity, start, end, size, timestamps):
        param = self.generate_request_param(entity, start, end, size, timestamps)
        if self.finance_report_type == 'FinanceGrowthAbility':
            from zvt.domain import FinanceGrowthAbility
            data_old = FinanceGrowthAbility.query_data(entity_id=entity.id)
        if self.finance_report_type == 'FinancePerShare':
            from zvt.domain import FinancePerShare
            data_old = FinancePerShare.query_data(entity_id=entity.id)

        if self.finance_report_type == 'FinanceProfitAbility':
            from zvt.domain import FinanceProfitAbility
            data_old = FinanceProfitAbility.query_data(entity_id=entity.id)

        if self.finance_report_type == 'FinanceReceivingAbility':
            from zvt.domain import FinanceReceivingAbility
            data_old = FinanceReceivingAbility.query_data(entity_id=entity.id)

        if 'pub_date' in data_old.columns:
            del data_old['pub_date']
        dict_ps = self.get_data_map2()
        data_pub_date = BalanceSheet.query_data(entity_id=entity.id, columns=['pub_date', 'id'])
        del data_pub_date['timestamp']
        df_old_all = pd.merge(data_old, data_pub_date, on=['id'])
        df_old_all.rename(columns=dict_ps, inplace=True)

        columns_map = {key: value[0] for key, value in self.get_data_map().items()}
        init_list = ['pub_date', 'id', 'entity_id', 'timestamp', 'provider', 'code', 'report_period', 'report_date']
        get_data_list = [i for i in columns_map if i not in df_old_all.columns and i not in init_list]
        choice_list = [j for k, j in columns_map.items() if k in get_data_list]

        em_code = to_em_entity_id(entity)
        df = pd.DataFrame()
        for reportdate in df_old_all.report_date.to_list():
            em_data = c.css(em_code, choice_list, "ispandas=1,TtmType=1,TradeDate=" + to_time_str(
                reportdate) + ",ReportDate=" + to_time_str(reportdate))
            if type(em_data) == pd.DataFrame:
                em_data['report_date'] = to_time_str(reportdate)
                df = df.append(em_data)
        if df.empty:
            return None
        df.rename(columns={value: key for key, value in columns_map.items()}, inplace=True)

        df = df.sort_values("report_date", ascending=True)
        if pd_is_not_null(df):
            df.rename(columns={value: key for key, value in columns_map.items()}, inplace=True)
            df['entity_id'] = entity.id

            def generate_id(se):
                return "{}_{}".format(se['entity_id'], to_time_str(se['report_date'], fmt=TIME_FORMAT_DAY))

            df['id'] = df[['entity_id', 'report_date']].apply(generate_id, axis=1)
            del df['entity_id'], df['report_date']
            data_res = pd.merge(df, df_old_all, on=['id'])
            data_res['provider'] = 'emquantapi'
            data_res['timestamp'] = data_res['pub_date']
            df_to_db(df=data_res, data_schema=self.data_schema, provider=self.provider, force_update=True)
        return None

    def record2(self, entity, start, end, size, timestamps):
        param = self.generate_request_param(entity, start, end, size, timestamps)

        if not end:
            end = to_time_str(now_pd_timestamp())
        start = to_time_str(start)
        em_code = to_em_entity_id(entity)
        df = pd.DataFrame()
        columns_map = {key: value[0] for key, value in self.get_data_map().items()}
        columns_list = list(columns_map.values())
        if self.finance_report_type == 'AuditOpinions':
            # 审计意见数据只有年报有
            param = [i for i in param if '12-31' in i]
        for reportdate in param:
            # 获取数据
            # 三大财务报表 使用ctr方法读取表名
            if self.data_type < 4:
                em_data = c.ctr(self.finance_report_type, columns_list,
                                "secucode=" + em_code + ",ReportDate=" + reportdate + ",ReportType=1")
                if em_data.Data == {}:
                    continue
                data = pd.DataFrame(em_data.Data['0']).T
                data.columns = em_data.Indicators
                data['report_date'] = reportdate
                df = df.append(data)
            # 否则用 css方法读取单个指标
            else:
                em_data = c.css(em_code, columns_list, "ispandas=1,ReportDate=" + reportdate)
                if type(em_data) == pd.DataFrame:
                    em_data['report_date'] = reportdate
                    if 'FIRSTNOTICEDATE' not in columns_list:
                        em_data['pub_date'] = end
                    df = df.append(em_data)
        if df.empty:
            return None
        df.rename(columns={value: key for key, value in columns_map.items()}, inplace=True)
        df = df.sort_values("report_date", ascending=True)
        if pd_is_not_null(df):
            df.rename(columns={value: key for key, value in columns_map.items()}, inplace=True)
            df['entity_id'] = entity.id
            df['timestamp'] = pd.to_datetime(df.report_date)
            df['provider'] = 'emquantapi'
            df['code'] = entity.code
            df['report_period'] = df['report_date'].apply(lambda x: to_report_period_type(x))

            def generate_id(se):
                return "{}_{}".format(se['entity_id'], to_time_str(se['timestamp'], fmt=TIME_FORMAT_DAY))

            df['id'] = df[['entity_id', 'timestamp']].apply(generate_id, axis=1)
            df_to_db(df=df, data_schema=self.data_schema, provider=self.provider, force_update=self.force_update)
        return None

    def get_original_time_field(self):
        return 'ReportDate'
