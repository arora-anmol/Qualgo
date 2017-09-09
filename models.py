import twitter_helper


def calculate_score(company_name):
    tweets = search_tweets(company_name)
    num = 0
    for tweet in tweets:
        num = get_sentiment(tweet) + num
    return


def search_tweets(search_term):
    return []


def get_sentiment(text):
    return 0
