import pandas as pd                        
from pytrends.request import TrendReq

def get_trends():
    print('getting trends')
    pytrend = TrendReq()
    kw_list = ["Blockchain", "Bitcoin", "Ethereum"]
    pytrend.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    related_queries = pytrend.related_queries()
    print(related_queries.values())
    # Interest by Region
    df_region = pytrend.interest_by_region()
    print(df_region.head(10))
    # Get Google Hot Trends data
    # df_trending = pytrend.trending_searches(pn='united_states')
    df_trending = pytrend.trending_searches()
    print(df_trending.head(100))
    print('****************interest over time****************')
    df_interest_time =pytrend.interest_over_time()
    print(df_interest_time.tail(5))
    print('****************top charts****************')
    df_top_charts = pytrend.top_charts(2021, hl='en-US', tz=300, geo='GLOBAL')
    print(df_top_charts.head(100))
