import pandas as pd                        
from pytrends.request import TrendReq

def get_trends():
    print('getting trends')
    pytrend = TrendReq()
    kw_list = ["Blockchain"]
    #pytrend.build_payload(kw_list=[‘Taylor Swift’])
    pytrend.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

    #pytrend.build_payload()
    # Interest by Region
    df = pytrend.interest_by_region()
    print(df.head(10))
    # Get Google Hot Trends data
    #df2 = pytrend.trending_searches(pn=’united_states’)
    df2 = pytrend.trending_searches(pn='united_states')
    print(df2.head())