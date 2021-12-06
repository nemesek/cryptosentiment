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

def get_sopr():
    print('*************getting sopr**************')
    # make API request
    week_ago = __get_time__(7)
    print(week_ago)
    res = requests.get('https://api.glassnode.com/v1/metrics/indicators/sopr',
        params={'a': 'BTC', 'api_key': config.glassnode_api_key, 's': week_ago}, verify=verify_cert)
    # convert to pandas dataframe
    sopr_df = pd.read_json(res.text, convert_dates=['t'])
    print(sopr_df)

def get_active_addresses():

    yesterday = __get_time__(1)
    print('*************getting active addresses**************')
    print(yesterday)
    # make API request
    res = requests.get('https://api.glassnode.com/v1/metrics/addresses/active_count',
        params={'a': 'BTC', 'api_key': config.glassnode_api_key, 'i':'1h', 's':yesterday }, verify=verify_cert)

    print(res.status_code)

    if (res.status_code != 200):
        print (res.status_code)
        print(res.reason)
        return
    # convert to pandas dataframe
    aa_df = pd.read_json(res.text, convert_dates=['t'])
    print(aa_df)


def get_futures_funding_rate():

    duration = __get_time__(30)
    print('*************getting futures funding rates**************')
    print(duration)
    # make API request
    res = requests.get('https://api.glassnode.com/v1/metrics/derivatives/futures_funding_rate_perpetual_all',
        params={'a': 'BTC', 'api_key': config.glassnode_api_key, 'i':'24h', 's':duration }, verify=verify_cert)

    print(res.status_code)

    if (res.status_code != 200):
        print (res.status_code)
        print(res.reason)
        return
    # convert to pandas dataframe
    aa_df = pd.read_json(res.text, convert_dates=['t'])
    print(aa_df)

def get_coin_days_destroyed():

    duration = __get_time__(30)
    print('*************getting coin days destroyed**************')
    print(duration)
    # make API request
    res = requests.get('https://api.glassnode.com/v1/metrics/indicators/cdd',
        params={'a': 'BTC', 'api_key': config.glassnode_api_key, 'i':'24h', 's':duration }, verify=verify_cert)

    print(res.status_code)

    if (res.status_code != 200):
        print (res.status_code)
        print(res.reason)
        return
    # convert to pandas dataframe
    aa_df = pd.read_json(res.text, convert_dates=['t'], dtype={"v": object})
    print(aa_df)

