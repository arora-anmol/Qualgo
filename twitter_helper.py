"""
import pickle
import os
import twitter

if not os.path.exists('secret_twitter_credentials.pkl'):
    Twitter = {}
    Twitter['Consumer Key'] = 'uzxnaq8pMVDJF5Ntc3t2grmA8'
    Twitter['Consumer Secret'] = 'o9zFjPznU2osyYKiUfzYKIeNAFQBFlC7X7AmzvcYUKq1EXQZ8C'
    Twitter['Access Token'] = '417904670-6AZ13uYEpp9REHI6DBLjWe6sF2IjbUXvmcZlL2Fl'
    Twitter['Access Token Secret'] = 'ADZtF6xx5UJlFGxgolHw6pUjfoqrWRwYe4GFIRnrxJoaO'
    with open('secret_twitter_credentials.pkl','wb') as f:
        pickle.dump(Twitter, f)
else:
    Twitter=pickle.load(open('secret_twitter_credentials.pkl','rb'))


auth = twitter.oauth.OAuth(Twitter['Access Token'],
                                  Twitter['Access Token Secret'],
                                  Twitter['Consumer Key'],
                                  Twitter['Consumer Secret'])

twitter_api = twitter.Twitter(auth=auth)

US_WOE_ID = 23424977
import json


def company_trend(topic):
    search_results = twitter_api.search.tweets(q = topic, result_type = 'popular')
    statuses = search_results['statuses']
    return search_results, statuses

search_results, statuses = company_trend("Yahoo")
"""