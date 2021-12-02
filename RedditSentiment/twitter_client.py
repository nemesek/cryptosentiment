#from twython import Twython
import tweepy
import config
# from auth import (
#     api_key,
#     api_secret,
#     access_token,
#     access_token_secret
# )

def __OAuth__():
    try:
        auth = tweepy.OAuthHandler(config.twitter_api_key, config.twitter_api_secret)
        auth.set_access_token(config.twitter_access_token, config.twitter_access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = __OAuth__()

def tweet_something():
    api = tweepy.API(oauth)
    #api.update_status(status='test post')
    recipient_id = "otrokentavos"  # ID of the user
    user = api.get_user(screen_name = 'acneme1')
    print(user.id)
    # users = api.lookup_users(screen_name=recipient_id)
    # print(len(users))
    # user_ids = [user.id_str for user in users]

    # for user_id in user_ids:
    #     print(user_id)
    #user_id = user.id_str
    #print(user_id)
    api.send_direct_message(user.id, "I love Cifa")
    print('done')

    # APP_KEY = consumer_key
    # APP_SECRET = consumer_secret

    #twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    # twitter = Twython(APP_KEY, APP_SECRET, bearer_token)
    # #ACCESS_TOKEN = twitter.obtain_access_token()
    # #print(ACCESS_TOKEN)
    # twitter.verify_credentials()
    # print('done')
    # twitter = Twython(
    #     api_key,
    #     api_secret,
    #     access_token, 
    #     access_token_secret
    # )

    # message = "Test Tweet"
    # twitter.update_status(status=message)
    # print("Tweeted: %s" % message)