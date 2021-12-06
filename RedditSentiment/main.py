import enum
import wordcounter, pandas as pd
import reddit_client as rc
from itertools import chain
import inspect
import glassnode_client as gc
import config
import twitter_client
import messari_client as mc

def build_permutations(list):
    permutated_list = []
    for item in list:
        permutated_list.append(item)
        permutated_list.append(item + 's')
        permutated_list.append(item + "'s")
        permutated_list.append(item + ",")

    return permutated_list

cryptos_normalized = {
    "BTC": build_permutations(["btc","bitcoin", "$btc"]),
    "ETH": build_permutations(["eth", "ethereum" "$eth"]),
    "SOL": build_permutations(["sol", "solana", "$sol"]),
    "ADA": build_permutations(["cardano", "ada", "$ada"]),
    "LRC": build_permutations(["lrc", "loopring", "$lrc"]),
    "ALGO": build_permutations(["algo", "algorand","$algo"]),
    "MATIC": build_permutations(["polygon", "matic", "$matic"]),
    "SAND": build_permutations(["sand", "sandbox", "$sand"]),
    "FTM": build_permutations(["ftm", "fantom","$ftm"]),
    "ONE": build_permutations(["harmony", "$one"] ),
    "LINK": build_permutations(["link", "chainlink", "$link"]),
    "IMX": build_permutations(["imx", "$imx", "immutable"]),
    "DYDX": build_permutations(["dydx", "$dydx"]),
    "CKB": build_permutations(["ckb", "$ckb", "nervos"]),
    "SYS": build_permutations(["sys", "$sys", "syscoin"]),
    "AVAX": build_permutations(["avax", "$avax", "avalanche"]),
    "LUNA": build_permutations(["luna", "$luna", "terra"]),
    "DOT": build_permutations(["dot", "$dot", "polkadot"]),
    "ATOM": build_permutations(["atom", "$atom", "cosmos"]),
    "HBAR": build_permutations(["hbar", "$hbar", "hedera", "hashgraph"]),
    "VXV": build_permutations(["vxv", "$vxv", "vectorspace"]),
}

def reduce_counts(dict1, dict2):
    count_by_token = {key: 0 for key in cryptos_normalized}
    for k,v in dict1.items():
        for k2,v2 in cryptos_normalized.items():
            if k in v2:
                count_by_token[k2] += v

    for k,v in dict2.items():
        for k2,v2 in cryptos_normalized.items():
            if k in v2:
                count_by_token[k2] += v

    # return count_by_token
    sorted_orders = sorted(count_by_token.items(), key=lambda x: x[1], reverse=True)
    return sorted_orders


def filter_cryptos(sentence_list):
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

# reddit stuff
# titles_and_comments = rc.get_posts()
# titles = titles_and_comments[0]
# comments = titles_and_comments[-1]

# cryptos_in_titles = filter_cryptos(titles)
# cryptos_in_comments = filter_cryptos(comments)
# title_counts = wordcounter.get_frequency_count(cryptos_in_titles)
# comment_counts = wordcounter.get_frequency_count(cryptos_in_comments)
# print('about to reduce')
# print(reduce_counts(title_counts, comment_counts))
# done with reddit stuff
# messari and glass node
mc.get_all_assets()
gc.get_sopr()
gc.get_active_addresses()
gc.get_futures_funding_rate()
gc.get_coin_days_destroyed()
#twitter_client.tweet_something()
# just testing something

