import json
import requests
import asyncio
import pandas as pd
import time
#from RedditSentiment.moving_average import moving_average 
import config
import request_helper as rh
import moving_average as ma

verify_cert = config.require_ssl_cert


def process_chain_data():
    # __get_sopr('btc')
    # __get_sopr('eth')
    # __get_active_addresses('btc')
    # __get_active_addresses('eth')
    # __get_futures_funding_rate()
    # __get_coin_days_destroyed('btc')
    # __get_coin_days_destroyed('eth')
    # __get_mvrv_info('btc')
    # __get_mvrv_info('eth')
    # __get_exchange_net_position_change('btc')
    # __get_nvt_data('btc')
    __get_nvt_data('eth')

def __get_time(numDays):
    now = (int)(time.time())
    numDays *= 86000
    return now - numDays

def __build_request(api, asset, duration, interval='24h'):
        res = requests.get('https://api.glassnode.com/' + api, params={'a': asset, 'api_key': config.glassnode_api_key, 'i':interval, 's':duration }, verify=verify_cert)
        return res

def __get_sopr(asset):
    print('*************getting ' + asset + ' sopr**************')
    week_ago = __get_time(7)
    res = __build_request(api='v1/metrics/indicators/sopr', asset=asset, duration=week_ago)    
    if rh.check_status_code(res) is True:
        sopr_df = pd.read_json(res.text, convert_dates=['t'], dtype={"v": object})
        print(sopr_df)

def __get_active_addresses(asset):
    yesterday = __get_time(1)
    print('*************getting ' + asset + ' active addresses**************')
    res = __build_request(api='v1/metrics/addresses/active_count', asset=asset, duration=yesterday, interval='1h')    
    if rh.check_status_code(res) is True:
        aa_df = pd.read_json(res.text, convert_dates=['t'], dtype={"v": object})
        print(aa_df)

def __get_futures_funding_rate():
    print('*************getting futures funding rates**************')
    duration = __get_time(30)
    res = __build_request(api='v1/metrics/derivatives/futures_funding_rate_perpetual_all', asset='BTC', duration=duration)    
    if rh.check_status_code(res) is True:
        ffr_df = pd.read_json(res.text, convert_dates=['t'], dtype={"v": object})
        print(ffr_df)

def __get_coin_days_destroyed(asset):
    print('*************getting ' + asset + ' coin days destroyed**************')
    duration = __get_time(30)
    res = __build_request(api='v1/metrics/indicators/cdd', asset=asset, duration=duration)    
    if rh.check_status_code(res) is True:
        cdd_df = pd.read_json(res.text, convert_dates=['t'], dtype={"v": object})
        print(cdd_df)

def __get_mvrv_info(asset):
    print('*************getting ' + asset + ' mvrv data**************')
    duration = __get_time(30)
    res1 = __build_request(api='v1/metrics/market/mvrv', asset=asset, duration=duration)
    if rh.check_status_code(res1) is True:
        mvrv_df = pd.read_json(res1.text, convert_dates=['t'])
        print(mvrv_df)
    
    print('*************getting ' + asset + ' mvrv z-score**************')
    res2 = __build_request(api='v1/metrics/market/mvrv_z_score', asset=asset, duration=duration)
    if rh.check_status_code(res2) is True:
        mvrvz_df = pd.read_json(res2.text, convert_dates=['t'])
        print(mvrvz_df)

def __get_exchange_net_position_change(asset):
    duration = __get_time(30)
    print('*************getting ' + asset + ' net exchange balance data**************')
    res = __build_request(api='v1/metrics/distribution/exchange_net_position_change', asset=asset, duration=duration)
    if rh.check_status_code(res) is True:
        df = pd.read_json(res.text, convert_dates=['t'])
        print(df)

def __get_nvt_data(asset):
    duration = __get_time(30)
    print('*************getting ' + asset + ' nvt signal**************')
    nvts_res = __build_request(api='v1/metrics/indicators/nvts', asset=asset, duration=duration)
    if rh.check_status_code(nvts_res) is True:
        df = pd.read_json(nvts_res.text, convert_dates=['t'])
        print(df)

    print('*************getting ' + asset + ' nvt ratio**************')
    nvtr_res = __build_request(api='v1/metrics/indicators/nvt', asset=asset, duration=duration)
    if rh.check_status_code(nvtr_res) is True:
        df = pd.read_json(nvtr_res.text, convert_dates=['t'])
        print(df)
        values = df.v.values  # df.v is a pandas.Series type
        #nvt_ra = ma.rollavg_cumsum(values, len(values) - 1)
        nvt_ma = ma.moving_average(values, 7)
        
        print(nvt_ma)
        most_recent = values[-1:]
        print('most recent is {mr}'.format(mr = most_recent))
        # print(most_recent)
        z = ma.compute_z_score(values, most_recent)
        print('z-score for today: {z}'.format(z=z))
        if abs(z) > 1:
            print('sigma move')
        else:
            print('not a sigma move')
        #print(nvt_ra)
