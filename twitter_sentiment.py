import tweepy

class TwitterSentiment(object):
    '''
    This class will fetch a particular tweeter user's frequent tweets, analyse the tweets and return the most used used words with their frequency
    '''
    #####  CLASS VARIABLES    ######
    
    #a list with stop words
    stop_words = ["a", "about", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

    
    #Variables that contains the user credentials to access Twitter API 
    API_KEYS='EzfVwFMj3IzAUXMzvXLX9gHaF'
    API_SECRET= "Y1Gnr2oklcYGFbTryr3yDiiXgIWKAmPUVyouyr4NbRg8wmsjMT"
    ACCESS_TOKEN = "588855017-vZ5eQksRsgei2Jc2Wfev22DY2yWdk748ds7EiHFb"
    ACCESS_TOKEN_SECRET = "dJvDBNYHxhDO67I1B61bsd7P7S1j1PCkee4LI7fLjVW2b"
    
    # OAuth Authentication. This is the authidication for using the twitter api
    auth = tweepy.OAuthHandler(API_KEYS, API_SECRET)
    auth.secure = True
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    #create an object of the twitter api
    api = tweepy.API(auth)
    
    
    def __init__(self, username):
        '''
        initialises the username whose data is to be fetched(tweets)
        '''
        
        self.username = username
        #print(TwitterSentiment.api.me().name)
        

    def fetch_data(self):
        '''
        This method fetchs data from twitter for a specific user and stores it in a json file
        '''
        my_dict = dict()
        alltweets = list()
        new_tweets = TwitterSentiment.api.user_timeline(self.username, count=200, max_id= 0)
        new_tweets = TwitterSentiment.api.user_timeline( self.username, count=200)
        alltweets.extend(new_tweets)
        if not alltweets:
            my_dict[0] = "No tweet so far","00/00/00"
            return my_dict
        
        oldest = alltweets[-1].id - 1
	
        #keep grabbing tweets until there are no tweets left to grab
        while new_tweets:
            new_tweets = TwitterSentiment.api.user_timeline(self.username, count=200, max_id=oldest)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
        #save the tweet text in a dictionary mapped against the specific tweet id    
        for tweet in alltweets:
            my_dict[tweet.id] = (tweet.text,tweet.created_at)
        return my_dict
    
    def display_tweets(self):
        tweet_dict = self.fetch_data()
        header='{} {} {}'.format("\nTWITTER ID".ljust(30) ,"DATE POSTED".ljust(30) ,"THE TWEET\n\n")
        print(header)
        for key in tweet_dict:
            print('{} {} {}'.format(str(key).ljust(30) , str(tweet_dict[key][1]).ljust(30) , tweet_dict[key][0]))
        
    
    def analyse_data(self):
        '''
        This method takes the json file created in fetch data method and analyses the most frequent tweets words for that  user eliminating the stop words.
        Return a with dictictionary where word is a key and the frequency is the value) 
        '''
        pass
    
user=  TwitterSentiment("emmanuelmuthui")
#
user.fetch_data()
user.display_tweets()

#user=  TwitterSentiment("Emmanuel")
#print (len(user.stop_words))

