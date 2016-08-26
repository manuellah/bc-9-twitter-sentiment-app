import tweepy, progressbar
from config import *

class TwitterSentiment(object):
    '''
    This class will fetch a particular tweeter user's frequent tweets, analyse the tweets and return the most used used words with their frequency
    '''
    
    # OAuth Authentication. This is the authidication for using the twitter api
    auth = tweepy.OAuthHandler(API_KEYS, API_SECRET)
    auth.secure = True
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    #create an object of the twitter api
    api = tweepy.API(auth)
    
    
    def __init__(self, username, number=3200):
        '''
        initialises the username whose data is to be fetched(tweets)
        '''
        
        self.username = username
        self.no_tweets = number
        

    def fetch_data(self ):
        '''
        This method fetchs data from twitter for a specific user and stores it in a json file
        '''
        my_dict = dict()
        alltweets = list()
        bar = progressbar.ProgressBar(max_value = self.no_tweets)
        print()
        if self.no_tweets <= 200:
            new_tweets = TwitterSentiment.api.user_timeline(self.username, count = self.no_tweets)
            alltweets.extend(new_tweets)
            if not alltweets:
                my_dict[0] = "No tweet so far","00/00/00"
                return my_dict

        else:    
            new_tweets = TwitterSentiment.api.user_timeline(self.username, count=200)
            alltweets.extend(new_tweets)
            self.no_tweets -= 200
            oldest = alltweets[-1].id - 1

            #keep grabbing tweets until there are no tweets left to grab
            while new_tweets:
                if self.no_tweets <= 200:
                    new_tweets = TwitterSentiment.api.user_timeline(self.username, count = self.no_tweets)
                    alltweets.extend(new_tweets)
                    
                else:
                    new_tweets = TwitterSentiment.api.user_timeline(self.username, count = 200, max_id = oldest)
                    alltweets.extend(new_tweets)
                    oldest = alltweets[-1].id - 1
                    self.no_tweets -= 200
                
        #save the tweet text in a dictionary mapped against the specific tweet id    
        for tweet in alltweets:
                my_dict[tweet.id] = (tweet.text, tweet.created_at)
        return my_dict
    
    def display_tweets(self):
        tweet_dict = self.fetch_data()
        header='{} {} {} {}'.format("\nTWITTER ID".ljust(30) ,"DATE POSTED".ljust(30) ,"THE TWEET\n\n", "=="*70)
        print(header)
        for key in tweet_dict:
            print('{} {} {}'.format(str(key).ljust(30) , str(tweet_dict[key][1]).ljust(30) , tweet_dict[key][0]))
        
    
    def analyse_data(self):
        '''
        This method takes the json file created in fetch data method and analyses the most frequent tweets words for that  user eliminating the stop words.
        Return a with dictictionary where word is a key and the frequency is the value) 
        '''
        tweet_dict = self.fetch_data()
        freq_dict = dict()
        for key in tweet_dict:
            tweet_words = str(tweet_dict[key][0]).lower().split()
            for word in tweet_words:
                if word in stop_words:
                    continue
                elif word not in list(freq_dict):
                    freq_dict[word] = 1
                else:
                    freq_dict[word] += 1
                    
        freq_list = [(freq_dict[key], key) for key in freq_dict]
        freq_list.sort()
        print('{} {} {} {} {} {}'.format("\n\n","COMMON TWEETED WORD".ljust(30), "THE FREQUENCY\n".ljust(30), '\n\n', "=="*70 , "\n\n"))
        for freq, word in freq_list[::-1]:
            print(' {} {}'.format(word.ljust(30), str(freq).ljust(30)))
    
        
#user=  TwitterSentiment("emmanuelmuthui",3)
#user.fetch_data()
#user.display_tweets()
#print(user.analyse_data())

#user=  TwitterSentiment("Emmanuel")
#print (len(user.stop_words))

