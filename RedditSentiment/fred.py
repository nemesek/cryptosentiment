import requests as req
import config
import request_helper as rh 

def get_categories():
    key = config.fred_api_key
    print('*************getting FRED data**************')
    #api = 'https://api.stlouisfed.org/fred/category?category_id=125&api_key=' + key + '&file_type=json'
    #api = 'https://api.stlouisfed.org/fred/release?release_id=53&api_key=' + key + '&file_type=json'
    #api = 'https://api.stlouisfed.org/fred/releases?&api_key=' + key + '&file_type=json'
    api = 'https://api.stlouisfed.org/fred/tags?&api_key=' + key + '&file_type=json'
    res = req.get(api)
    if rh.check_status_code(res) is True:
        print(res.text)
