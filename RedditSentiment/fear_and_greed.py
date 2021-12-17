import requests
import stats
import request_helper as rh
import json


def __process_today(values):
    today = values[0]
    todays_score = today["value"]
    todays_classification = today["value_classification"]
    print("current score is: {score}".format(score=todays_score))
    print("current classification is: " + todays_classification)
    return todays_score

def get_fear_and_greed():
    api = 'https://api.alternative.me/fng/?limit=30'
    res = requests.get(api)
    if not rh.check_status_code(res):
        print('something wrong with fear and greed index')
        return
    
    fg_dict = json.loads(res.text)
    values = fg_dict["data"]

    print('*************crypto fear and greed data**************')
    todays_score = __process_today(values)
    score_values = list(map(lambda val: int(val["value"]), values)) 
    z_score = stats.compute_z_score(score_values, todays_score)
    print("fear and greed z-score {z}".format(z=z_score))
    #mean = stats.compute_mean(score_values)
    num_days = len(score_values)
    mean = sum(score_values)/num_days
    print("{days} day mean is {avg}".format(days=num_days,avg=mean))



