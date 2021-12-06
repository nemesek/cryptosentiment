import praw
import config

def get_posts():
    reddit = praw.Reddit(
    client_id=config.reddit_client_id,
    client_secret = config.reddit_client_secret,
    user_agent="my user agent"
    )

    submission_titles = []
    submission_comments = []
    for submission in reddit.subreddit("cryptocurrency").hot(limit=10):
        submission_titles.append(submission.title)
        for comment in submission.comments.list():
            if not hasattr(comment, 'body'):
                continue
            submission_comments.append(comment.body)

    return (submission_titles, submission_comments)


# import pip._vendor.requests as requests, pandas as pd
# import config

# def get_posts():

#     # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
#     auth = requests.auth.HTTPBasicAuth('snvxbdQiMNm03isjrqhkyw', '9SLK8uG7DQ7B5ZtisuPTk3WtL8jGEw')

#     # here we pass our login method (password), username, and password
#     data = {'grant_type': 'password',
#             'username': config.reddit_username,
#             'password': config.reddit_password}

#     # setup our header info, which gives reddit a brief description of our app
#     headers = {'User-Agent': 'MyBot/0.0.1'}

#     # send our request for an OAuth token
#     res = requests.post('https://www.reddit.com/api/v1/access_token',
#                         auth=auth, data=data, headers=headers)

#     # convert response to JSON and pull access_token value
#     TOKEN = res.json()['access_token']

#     # add authorization to our headers dictionary
#     headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

#     # while the token is valid (~2 hours) we just add headers=headers to our requests
#     #requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
#     res = requests.get("https://oauth.reddit.com/r/cryptocurrency/hot", headers=headers, params={'limit': '2'})
#     # res2 = requests.get("https://oauth.reddit.com/comments/qtveh1?sort=old, threaded=false", headers=headers)

#     # print(res2.json())  # let's see what we get
#     # """ for post in res.json()['data']['children']:
#     #     print(post['data']['title']) """

#     df = pd.DataFrame()  # initialize dataframe
#     counter = 0
#     # loop through each post retrieved from GET request
#     for post in res.json()['data']['children']:
#         # append relevant data to dataframe
#         df = df.append({
#             'subreddit': post['data']['subreddit'],
#             'title': post['data']['title'],
#             'selftext': post['data']['selftext'],
#             'upvote_ratio': post['data']['upvote_ratio'],
#             'ups': post['data']['ups'],
#             'downs': post['data']['downs'],
#             'score': post['data']['score'],
#             'id': post['data']['id']
#         }, ignore_index=True)
#     print('done')
#     return df