import reddit_client as rc
import glassnode_client as gc
import twitter_client as tc
import messari_client as mc
import requests
import request_helper as rh
from datetime import datetime
import json

def __process_fear_and_greed_data(fg_dict):
    values = fg_dict["data"]
    total = 0
    num_days = len(values)
    today = values[0]
    todays_score = today["value"]
    todays_classification = today["value_classification"]

    print("current score is: {score}".format(score=todays_score))
    print("current classification is: " + todays_classification)
    
    for item in values:
        #ts = int(item["timestamp"])
        total += int(item["value"])
        #print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
    simple_average = total / num_days
    print("25 day simple average is {avg}".format(avg=simple_average))
    
def __get_fear_and_greed():
    api = 'https://api.alternative.me/fng/?limit=25'
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
#gc.process_chain_data()
__get_fear_and_greed()
#twitter_client.tweet_something()

