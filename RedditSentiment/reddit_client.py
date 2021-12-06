import praw
import config
import wordcounter


def process_sentiment():
    titles_and_comments = __get_posts()
    titles = titles_and_comments[0]
    comments = titles_and_comments[-1]

    cryptos_in_titles = __filter_cryptos(titles)
    cryptos_in_comments = __filter_cryptos(comments)
    title_counts = wordcounter.get_frequency_count(cryptos_in_titles)
    print('title count')
    print(__reduce_count(title_counts))
    comment_counts = wordcounter.get_frequency_count(cryptos_in_comments)
    print('comment count')
    print(__reduce_count(comment_counts))


def __build_permutations(list):
    permutated_list = []
    for item in list:
        permutated_list.append(item)
        permutated_list.append(item + 's')
        permutated_list.append(item + "'s")
        permutated_list.append(item + ",")

    return permutated_list

cryptos_normalized = {
    "BTC": __build_permutations(["btc","bitcoin", "$btc"]),
    "ETH": __build_permutations(["eth", "ethereum" "$eth"]),
    "SOL": __build_permutations(["sol", "solana", "$sol"]),
    "ADA": __build_permutations(["cardano", "ada", "$ada"]),
    "LRC": __build_permutations(["lrc", "loopring", "$lrc"]),
    "ALGO": __build_permutations(["algo", "algorand","$algo"]),
    "MATIC": __build_permutations(["polygon", "matic", "$matic"]),
    "SAND": __build_permutations(["sand", "sandbox", "$sand"]),
    "FTM": __build_permutations(["ftm", "fantom","$ftm"]),
    "ONE": __build_permutations(["harmony", "$one"] ),
    "LINK": __build_permutations(["link", "chainlink", "$link"]),
    "IMX": __build_permutations(["imx", "$imx", "immutable"]),
    "DYDX": __build_permutations(["dydx", "$dydx"]),
    "CKB": __build_permutations(["ckb", "$ckb", "nervos"]),
    "SYS": __build_permutations(["sys", "$sys", "syscoin"]),
    "AVAX": __build_permutations(["avax", "$avax", "avalanche"]),
    "LUNA": __build_permutations(["luna", "$luna", "terra"]),
    "DOT": __build_permutations(["dot", "$dot", "polkadot"]),
    "ATOM": __build_permutations(["atom", "$atom", "cosmos"]),
    "HBAR": __build_permutations(["hbar", "$hbar", "hedera", "hashgraph"]),
    "VXV": __build_permutations(["vxv", "$vxv", "vectorspace"]),
}

def __reduce_count(dict1):
    count_by_token = {key: 0 for key in cryptos_normalized}
    for k,v in dict1.items():
        for k2,v2 in cryptos_normalized.items():
            if k in v2:
                count_by_token[k2] += v
    
    filtered_count = {}
    for k,v in count_by_token.items():
        if v != 0:
            filtered_count[k] = v
    # return count_by_token
    sorted_orders = sorted(filtered_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_orders


def __filter_cryptos(sentence_list):
    return_list = []
    my_2d_list = list(cryptos_normalized.values())
    cryptos = [cell for row in my_2d_list for cell in row]

    for sentence in sentence_list:
        words =  sentence.split()
        for word in words:
            lower_case_word = word.lower()
            if lower_case_word in cryptos:
                return_list.append(lower_case_word)
    return return_list

def __get_posts():
    reddit = praw.Reddit(
    client_id=config.reddit_client_id,
    client_secret = config.reddit_client_secret,
    user_agent="my user agent"
    )

    submission_titles = []
    submission_comments = []
    for submission in reddit.subreddit("cryptocurrency").hot(limit=25):
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