from messari.messari import Messari
import config
import requests
import pandas as pd
import fsspec
import json

def process_messari_data():
    m = Messari(config.messari_api_key)
    __get_all_assets(m)
    __get_metric_timeseries(m)
    __get_news()
    # __get_asset_news()

def __get_all_assets(m):
    print('Current pricing')
    response_data_df = m.get_all_assets(asset_fields=['metrics'], to_dataframe=True)
    head = response_data_df.head()
    print(head)

def __get_metric_timeseries(m):
    print('Bitcoin and Eth 2nd half 2020 data')
    assets = ['btc', 'eth']
    metric = 'price'
    start = '2020-06-01'
    end = '2021-01-01'
    timeseries_df = m.get_metric_timeseries(asset_slugs=assets, asset_metric=metric, start=start, end=end)
    print(timeseries_df)

def __get_news():
    print('Getting news for everything')
    either = __get_response('https://data.messari.io/api/v1/news?fields=title,tags')
    if either[0] == True:
        res = either[1]
        news = json.loads(res.text)
        news_list = news['data']
        for item in news_list:
            print('title: ' + item['title'] + ' ****Tags**** : ' + ', '.join(item['tags']))
            # #print(item['tags'])
        return

    print("Error: " + either[1])

def __get_asset_news():
    print('Getting news for asset')
    either = __get_response('https://data.messari.io/api/v1/news/btc')
    if either[0] == True:
        res = either[1]
        news = json.loads(res.text)
        news_list = news['data']
        for a in news_list:
            print(a)
        return

    print("Error: " + either[1])  

def __get_response(url):
    res = requests.get(url)
    if (res.status_code != 200):
        print('Houston we have a ')
        print (res.status_code)
        print(res.reason)
        return (False, res.reason)
    return (True, res)