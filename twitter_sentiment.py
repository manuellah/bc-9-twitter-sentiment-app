class TwitterSentiment(object):
    '''
    This class will fetch a particular tweeter user's frequent tweets, analyse the tweets and return the most used used words with their frequency
    '''
    #a list with stop words
    stop_words = []
    
    def __init__(self, username):
        '''
        initialises the username whose data is to be fetched(tweets)
        '''
        self.username = username
        
    def fetch_data(self):
        '''
        This method fetchs data from twitter for a specific user and stores it in a json file
        '''
        pass
    
    def analyse_data(self):
        '''
        This method takes the json file created in fetch data method and analyses the most frequent tweets words for that  user eliminating the stop words.
        Return a with dictictionary where word is a key and the frequency is the value) 
        '''
        pass