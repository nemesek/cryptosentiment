from messari.messari import Messari
import config

def get_all_assets():
    #  m = Messari(config.messari_api_key)
    #  baz = inspect.getmembers(m, inspect.isfunction)
    #  print(baz)
    #  print(m)
    #  assets = ['btc', 'eth']
    #  metric = 'price'
    #  start = '2020-06-01'
    #  end = '2021-01-01'
    #  print('yo2')
     #timeseries_df = m.get_metric_timeseries(asset_slugs=assets, asset_metric=metric, start=start, end=end)
     #print(timeseries_df)
     m = Messari(config.messari_api_key)
     response_data_df = m.get_all_assets(asset_fields=['metrics'], to_dataframe=True)
     head = response_data_df.head()
     print(head)
    # print('hi from Messari')
    # print(config.messari_api_key)