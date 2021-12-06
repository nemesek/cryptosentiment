import json
import requests
import asyncio
import pandas as pd
import time 
# insert your API key here
import config

verify_cert = config.require_ssl_cert

def __get_time__(numDays):
    now = (int)(time.time())
    #yesterday = time.localtime(now - 86400)
    numDays *= 86000
    return now - numDays

def __build_request__(api, asset, duration, interval='24h'):
        res = requests.get('https://api.glassnode.com/' + api, params={'a': asset, 'api_key': config.glassnode_api_key, 'i':interval, 's':duration }, verify=verify_cert)
        return res

def __check_status_code__(res):
        if (res.status_code != 200):
            print (res.status_code)
            print(res.reason)
            return False
        return True

def get_sopr(asset):
    print('*************getting ' + asset + ' sopr**************')
    week_ago = __get_time__(7)
    res = __build_request__(api='v1/metrics/indicators/sopr', asset=asset, duration=week_ago)    
    if __check_status_code__(res) is True:
        sopr_df = pd.read_json(res.text, convert_dates=['t'], dtype={"v": object})
        print(sopr_df)

def get_active_addresses(asset):
    yesterday = __get_time__(1)
    print('*************getting ' + asset + ' active addresses**************')
    res = __build_request__(api='v1/metrics/addresses/active_count', asset=asset, duration=yesterday, interval='1h')    
    if __check_status_code__(res) is True:
        aa_df = pd.read_json(res.text, convert_dates=['t'], dtype={"v": object})
        print(aa_df)

def get_futures_funding_rate():
    print('*************getting futures funding rates**************')
    duration = __get_time__(30)
    res = __build_request__(api='v1/metrics/derivatives/futures_funding_rate_perpetual_all', asset='BTC', duration=duration)    
    if __check_status_code__(res) is True:
        ffr_df = pd.read_json(res.text, convert_dates=['t'], dtype={"v": object})
        print(ffr_df)

def get_coin_days_destroyed(asset):
    print('*************getting ' + asset + ' coin days destroyed**************')
    duration = __get_time__(30)
    res = __build_request__(api='v1/metrics/indicators/cdd', asset=asset, duration=duration)    
    if __check_status_code__(res) is True:
        cdd_df = pd.read_json(res.text, convert_dates=['t'], dtype={"v": object})
        print(cdd_df)

def get_mvrv_info(asset):
    print('*************getting ' + asset + ' mvrv data**************')
    duration = __get_time__(30)
    res1 = __build_request__(api='v1/metrics/market/mvrv', asset=asset, duration=duration)
    if __check_status_code__(res1) is True:
        mvrv_df = pd.read_json(res1.text, convert_dates=['t'])
        print(mvrv_df)
    
    print('*************getting ' + asset + ' mvrv z-score**************')
    res2 = __build_request__(api='v1/metrics/market/mvrv_z_score', asset=asset, duration=duration)
    if __check_status_code__(res2) is True:
        mvrvz_df = pd.read_json(res2.text, convert_dates=['t'])
        print(mvrvz_df)