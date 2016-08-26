import tweepy
import csv
import argparse
#https://dev.twitter.com/rest/reference/get/statuses/user_timeline(timeline output pic)

API_KEYS='EzfVwFMj3IzAUXMzvXLX9gHaF'
API_SECRET= "Y1Gnr2oklcYGFbTryr3yDiiXgIWKAmPUVyouyr4NbRg8wmsjMT"
ACCESS_TOKEN = "588855017-vZ5eQksRsgei2Jc2Wfev22DY2yWdk748ds7EiHFb"
ACCESS_TOKEN_SECRET = "dJvDBNYHxhDO67I1B61bsd7P7S1j1PCkee4LI7fLjVW2b"

auth = tweepy.OAuthHandler(API_KEYS, API_SECRET)
#auth.secure = True
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

################ MY authedication up   ###############



def get_all_tweets(screen_name):
    my_dict = dict()
    alltweets = list()
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    if not alltweets:
        my_dict[0] = "No tweet so far","00/00/00"
        return my_dict
    
    
    oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
    while new_tweets:
        new_tweets = api.user_timeline(screen_name = screen_name, count=200, max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
    #save the tweet text in a dictionary mapped against the specific tweet id    
    for tweet in alltweets:
        my_dict[tweet.id] = (tweet.text,tweet.created_at)
        
    return my_dict

def display_tweets():
    tweet_dict = get_all_tweets("emmanuelmuthui")
    header='{} {} {}'.format("tweeter id".ljust(30),"Date Posted".ljust(30) ,"The Tweet")
    print(header)
    for key in tweet_dict:
        print('{} {} {}'.format(str(key).ljust(30), str(tweet_dict[key][1]).ljust(30) , tweet_dict[key][0]))
        
def frequency_analyzer():
    tweet_dict = get_all_tweets("emmanuelmuthui")
    string_list = list()
    freq_dict = dict()
    for key in tweet_dict:
        tweet_list = str(tweet_dict[key][0]).split()
        for word in tweet_list:
            if word in stop_words:
                continue
            elif word not in list(freq_dict):
                freq_dict[word] = 1
            freq_dict[word] += 1
            
                
        


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

    
