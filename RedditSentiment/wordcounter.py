from collections import Counter

def get_frequency_count(list_of_words):
    #list1=['apple','egg','apple','banana','egg','apple']
    return Counter(list_of_words)
    # Counter({'apple': 3, 'egg': 2, 'banana': 1})