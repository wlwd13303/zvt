# -*- coding: utf-8 -*-

import pandas as pd
from zvt.contract.api import df_to_db
from zvt.contract.recorder import Recorder, TimeSeriesDataRecorder
from zvt.recorders.emquantapi.common import mainCallback
from zvt.recorders.joinquant.common import to_entity_id
from zvt.utils.pd_utils import pd_is_not_null
from zvt.utils.time_utils import now_pd_timestamp, to_time_str, TIME_FORMAT_DAY
from zvt.domain import BlockStock, Block, Block1dKdata, BlockMoneyFlow
from zvt.settings import ZVT_HOME
try:
    from jqdatasdk import finance, query
    from EmQuantAPI import *
except:
    pass

class EmChinaBlockRecorder(Recorder):
    """
    choice板块数据
    """
    provider = 'emquantapi'
    data_schema = Block

    hs_category_map = pd.read_excel(f'{ZVT_HOME}/data/沪深股票GICS行业分类.xlsx')
    hk_category_map = pd.read_excel(f'{ZVT_HOME}/data/港股GICS行业分类.xlsx')
    us_category_map = pd.read_excel(f'{ZVT_HOME}/data/美股GICS行业分类.xlsx')
    gics_one = hs_category_map[['一级板块代码','一级板块名称']].append(hk_category_map[['一级板块代码','一级板块名称']]).append(us_category_map[['一级板块代码','一级板块名称']]).dropna(subset=['一级板块名称'])
    gics_two = hs_category_map[['二级板块代码','二级板块名称']].append(hk_category_map[['二级板块代码','二级板块名称']]).append(us_category_map[['二级板块代码','二级板块名称']]).dropna(subset=['二级板块名称'])
    gics_three = hs_category_map[['三级板块代码','三级板块名称']].append(hk_category_map[['三级板块代码','三级板块名称']]).append(us_category_map[['三级板块代码','三级板块名称']]).dropna(subset=['三级板块名称'])
    gics_four = hs_category_map[['四级板块代码','四级板块名称']].append(hk_category_map[['四级板块代码','四级板块名称']]).append(us_category_map[['四级板块代码','四级板块名称']]).dropna(subset=['四级板块名称'])
    gics_one['一级板块代码'] = gics_one['一级板块代码'].apply(lambda x:str(int(x)).zfill(6))
    gics_two['二级板块代码'] = gics_two['二级板块代码'].apply(lambda x:str(int(x)).zfill(9))
    gics_three['三级板块代码'] = gics_three['三级板块代码'].apply(lambda x:str(int(x)).zfill(12))
    gics_four['四级板块代码'] = gics_four['四级板块代码'].apply(lambda x:str(int(x)).zfill(15))
    category_map=[]
    category_map.extend(gics_one.to_dict(orient='records'))
    category_map.extend(gics_two.to_dict(orient='records'))
    category_map.extend(gics_three.to_dict(orient='records'))
    category_map.extend(gics_four.to_dict(orient='records'))

    def __init__(self, batch_size=10, force_update=True, sleeping_time=10) -> None:
        super().__init__(batch_size, force_update, sleeping_time)

        # 调用登录函数（激活后使用，不需要用户名密码）
        loginResult = c.start("ForceLogin=1", '', mainCallback)
        if (loginResult.ErrorCode != 0):
            print("login in fail")
            exit()

    def run(self):
        # get stock blocks from sina
        for category_map_dict in self.category_map:
            # df = get_industries(name=category, date=None)
            category, name_ch = category_map_dict.items()
            df = pd.DataFrame(index=[0])
            if '一级板块代码' in category:
                df['code'] = category[1]
                if category[1].startswith('003'):
                    df['exchange'] = 'cn'
                elif category[1].startswith('204'):
                    df['exchange'] = 'us'
                elif category[1].startswith('402'):
                    df['exchange'] = 'hk'
                df['block_type'] = 'gicsl1'
            elif '二级板块代码' in category:
                df['code'] = category[1]
                if category[1].startswith('003'):
                    df['exchange'] = 'cn'
                elif category[1].startswith('204'):
                    df['exchange'] = 'us'
                elif category[1].startswith('402'):
                    df['exchange'] = 'hk'
                df['block_type'] = 'gicsl2'
            elif '三级板块代码' in category:
                df['code'] = category[1]
                if category[1].startswith('003'):
                    df['exchange'] = 'cn'
                elif category[1].startswith('204'):
                    df['exchange'] = 'us'
                elif category[1].startswith('402'):
                    df['exchange'] = 'hk'
                df['block_type'] = 'gicsl3'
            elif '四级板块代码' in category:
                df['code'] = category[1]
                if category[1].startswith('003'):
                    df['exchange'] = 'cn'
                elif category[1].startswith('204'):
                    df['exchange'] = 'us'
                elif category[1].startswith('402'):
                    df['exchange'] = 'hk'
                df['block_type'] = 'gicsl4'
            df['timestamp'] = now_pd_timestamp()
            df['name'] = name_ch[1]
            df['entity_type'] = 'block'
            df['category'] = "industry"
            df['id'] = df['entity_id'] = df.apply(lambda x: "block_" + x.exchange + "_" + x.code, axis=1)
            df_to_db(data_schema=self.data_schema, df=df, provider=self.provider,
                     force_update=True)
            self.logger.info(f"完成choice数据行业数据保存:{category[1],name_ch[1]}")


class EmChinaBlockStockRecorder(TimeSeriesDataRecorder):
    entity_provider = 'joinquant'
    entity_schema = Block

    provider = 'emquantapi'
    data_schema = BlockStock

    def __init__(self, entity_type='block', exchanges=None, entity_ids=None, codes=None, batch_size=10,
                 force_update=True, sleeping_time=5, default_size=2000, real_time=False, fix_duplicate_way='add',
                 start_timestamp=None, end_timestamp=None, close_hour=0, close_minute=0) -> None:
        super().__init__(entity_type, exchanges, entity_ids, codes, batch_size, force_update, sleeping_time,
                         default_size, real_time, fix_duplicate_way, start_timestamp, end_timestamp, close_hour,
                         close_minute)
        # 调用登录函数（激活后使用，不需要用户名密码）
        loginResult = c.start("ForceLogin=1", '', mainCallback)
        if (loginResult.ErrorCode != 0):
            print("login in fail")
            exit()

    def record(self, entity, start, end, size, timestamps):
        if not entity.block_type:
            return
        if 'gics' not in entity.block_type:
            return None
        # industry_stocks = get_industry_stocks(entity.code,date=now_pd_timestamp())
        industry_stocks = c.sector(entity.code, to_time_str(now_pd_timestamp()))
        if len(industry_stocks.Data) == 0:
            return None

        codes = industry_stocks.Codes
        names = [i for i in industry_stocks.Data if i not in codes]
        df = pd.DataFrame({"stock": codes,"stock_name":names})
        df["stock_id"] = df.stock.apply(lambda x: to_entity_id(x, "stock").lower())
        df["stock_code"] = df.stock_id.str.split("_", expand=True)[2]
        df["code"] = entity.code
        df["exchange"] = entity.exchange
        df["name"] = entity.name
        df["timestamp"] = now_pd_timestamp()
        df["entity_id"] = entity.id
        df["block_type"] = entity.block_type
        df["entity_type"] = "block"
        df["id"] = df.apply(lambda x: x.entity_id + "_" + x.stock_id, axis=1)
        if df.empty:
            return None
        df_to_db(data_schema=self.data_schema, df=df, provider=self.provider,
                 force_update=True)

        self.logger.info('finish recording BlockStock:{},{}'.format(entity.category, entity.name))


class JqChinaBlockKdataRecorder(TimeSeriesDataRecorder):
    entity_provider = 'joinquant'
    entity_schema = Block

    provider = 'emquantapi'
    data_schema = Block1dKdata

    def __init__(self, entity_type='block', exchanges=None, entity_ids=None, codes=None, batch_size=10,
                 force_update=True, sleeping_time=5, default_size=2000, real_time=False, fix_duplicate_way='add',
                 start_timestamp=None, end_timestamp=None, close_hour=0, close_minute=0) -> None:
        super().__init__(entity_type, exchanges, entity_ids, codes, batch_size, force_update, sleeping_time,
                         default_size, real_time, fix_duplicate_way, start_timestamp, end_timestamp, close_hour,
                         close_minute)

        # 调用登录函数（激活后使用，不需要用户名密码）
        loginResult = c.start("ForceLogin=1", '', mainCallback)
        if (loginResult.ErrorCode != 0):
            print("login in fail")
            exit()

    # def record(self, entity, start, end, size, timestamps):
    #     # if entity.exchange == "swl1":
    #     #     return None
    #     if not end:
    #         if (now_pd_timestamp() - start).days > 365:
    #             from datetime import timedelta
    #             end = to_time_str(start + timedelta(days=365))
    #         else:
    #             end = to_time_str(now_pd_timestamp())
    #     start = to_time_str(start)
    #     if entity.code in ['801780', '801180', '801150', '801160', '801230', '801890',
    #                    '801720', '801710', '801110', '801880', '801120', '801080',
    #                    '801750', '801170', '801140', '801770', '801760', '801010',
    #                    '801200', '801030', '801050', '801790', '801730', '801210',
    #                    '801740', '801020', '801130', '801040']:
    #         return None
    #     entityid = entity.id.replace('cn', 'swl3')
    #     df = get_data(data_schema=Block1dKdata, entity_id=entityid,provider='joinquant')
    #
    #     # df = c.csd(f"{entity.code}.SWI", "OPEN,CLOSE,HIGH,LOW,VOLUME,AMOUNT", start, end,
    #     #            "period=1,adjustflag=1,curtype=1,order=1,ispandas=1")
    #     if type(df) != pd.DataFrame:
    #         return None
    #     if pd_is_not_null(df):
    #         df['entity_id'] = entity.id
    #         df['provider'] = 'emquantapi'
    #
    #         def generate_kdata_id(se):
    #             return "{}_{}".format(se['entity_id'], to_time_str(se['timestamp'], fmt=TIME_FORMAT_DAY))
    #
    #         df['id'] = df[['entity_id', 'timestamp']].apply(generate_kdata_id, axis=1)
    #
    #         df_to_db(df=df, data_schema=self.data_schema, provider=self.provider, force_update=self.force_update)
    #
    #     return None

    def record(self, entity, start, end, size, timestamps):
        # if entity.exchange == "swl1":
        #     return None
        if not end:
            if (now_pd_timestamp() - start).days > 365:
                from datetime import timedelta
                end = to_time_str(start + timedelta(days=365))
            else:
                end = to_time_str(now_pd_timestamp())
        start = to_time_str(start)

        df = c.csd(f"{entity.code}.SWI", "OPEN,CLOSE,HIGH,LOW,VOLUME,AMOUNT", start, end,
                   "period=1,adjustflag=1,curtype=1,order=1,ispandas=1")
        if type(df) != pd.DataFrame:
            return None
        df.rename(columns={
            'DATES': 'timestamp',
            'OPEN': 'open',
            'CLOSE': 'close',
            'HIGH': 'high',
            'LOW': 'low',
            'VOLUME': 'volume',
            'AMOUNT': 'turnover',
        }, inplace=True)

        if pd_is_not_null(df):
            df['name'] = entity.name
            df['entity_id'] = entity.id
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['provider'] = 'joinquant'
            df['level'] = '1d'
            df['code'] = entity.code

            def generate_kdata_id(se):
                return "{}_{}".format(se['entity_id'], to_time_str(se['timestamp'], fmt=TIME_FORMAT_DAY))

            df['id'] = df[['entity_id', 'timestamp']].apply(generate_kdata_id, axis=1)

            df_to_db(df=df, data_schema=self.data_schema, provider=self.provider, force_update=self.force_update)

        return None


class JqChinaBlockMoneyFlowRecorder(TimeSeriesDataRecorder):
    # entity_provider = 'joinquant'
    # entity_schema = Block

    provider = 'emquantapi'
    data_schema = BlockMoneyFlow

    def __init__(self, entity_type='block', exchanges=None, entity_ids=None, codes=None, batch_size=10,
                 force_update=True, sleeping_time=5, default_size=2000, real_time=False, fix_duplicate_way='add',
                 start_timestamp=None, end_timestamp=None, close_hour=0, close_minute=0) -> None:
        super().__init__(entity_type, exchanges, entity_ids, codes, batch_size, force_update, sleeping_time,
                         default_size, real_time, fix_duplicate_way, start_timestamp, end_timestamp, close_hour,
                         close_minute)

        # 调用登录函数（激活后使用，不需要用户名密码）
        loginResult = c.start("ForceLogin=1", '', mainCallback)
        if (loginResult.ErrorCode != 0):
            print("login in fail")
            exit()

    def record(self, entity, start, end, size, timestamps):
        if "swl1" not in entity.id:
            return None
        start = to_time_str(start)
        df = finance.run_query(
            query(finance.SW1_DAILY_PRICE).filter(
                finance.SW1_DAILY_PRICE.code == entity.code).filter(
                finance.SW1_DAILY_PRICE.date >= start).limit(size))
        if pd_is_not_null(df):
            df['name'] = entity.name
            df.rename(columns={'money': 'turnover', 'date': 'timestamp'}, inplace=True)

            df['entity_id'] = entity.id
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['provider'] = 'joinquant'
            df['level'] = '1d'
            df['code'] = entity.code

            def generate_kdata_id(se):
                return "{}_{}".format(se['entity_id'], to_time_str(se['timestamp'], fmt=TIME_FORMAT_DAY))

            df['id'] = df[['entity_id', 'timestamp']].apply(generate_kdata_id, axis=1)

            df_to_db(df=df, data_schema=self.data_schema, provider=self.provider, force_update=self.force_update)

        return None


__all__ = ['EmChinaBlockRecorder', 'EmChinaBlockStockRecorder']

if __name__ == '__main__':
    # init_log('sina_china_stock_category.log')

    recorder = EmChinaBlockStockRecorder()
    recorder.run()
