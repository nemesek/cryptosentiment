import reddit_client as rc
import glassnode_client as gc
import twitter_client as tc
import messari_client as mc
import google_trends as gt
import fear_and_greed as fg
import fred



# reddit stuff
#rc.process_sentiment()
## done with reddit stuff
# #messari and glass node
#mc.process_messari_data() 
gc.process_chain_data()
fg.get_fear_and_greed()
fred.get_categories()
#gt.get_trends()
#twitter_client.tweet_something()

