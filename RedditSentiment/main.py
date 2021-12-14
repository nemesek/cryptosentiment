import reddit_client as rc
import glassnode_client as gc
import twitter_client as tc
import messari_client as mc
import requests
import request_helper as rh
from datetime import datetime
import json
import google_trends as gt
import moving_average as ma

def __process_fear_and_greed_data(fg_dict):
    print('*************crypto fear and greed data**************')
    values = fg_dict["data"]
    score_values = []
    total = 0
    num_days = len(values)
    today = values[0]
    todays_score = today["value"]
    todays_classification = today["value_classification"]

    print("current score is: {score}".format(score=todays_score))
    print("current classification is: " + todays_classification)
    
    for item in values:
        #ts = int(item["timestamp"])
        val = int(item["value"])
        total += val
        score_values.append(val)
        #print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
    mean = total / num_days
    print("25 day mean is {avg}".format(avg=mean))
    z_score = ma.compute_z_score(score_values, todays_score)
    print("fear and greed z-score {z}".format(z=z_score))
    
def __get_fear_and_greed():
    api = 'https://api.alternative.me/fng/?limit=30'
    res = requests.get(api)
    if not rh.check_status_code(res):
        print('something wrong with fear and greed index')
        return
    
    fg_dict = json.loads(res.text)
    __process_fear_and_greed_data(fg_dict)
    # print(res.text)

# reddit stuff
#rc.process_sentiment()
## done with reddit stuff
# #messari and glass node
#mc.process_messari_data() 
gc.process_chain_data()
__get_fear_and_greed()
#gt.get_trends()
#twitter_client.tweet_something()

