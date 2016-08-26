
"""Greeter.

Usage:
  app_main.py  <twitter_handle>  <number_of_tweets>
  app_main.py display_tweets <twitter_handle>  <number_of_tweets>
  app_main.py analyse_tweets <twitter_handle>  <number_of_tweets>
  app_main.py (-h | --help)

Options:
  -h --help         Show this screen.
 

"""
from docopt import docopt
from colorama import *
from twitter_sentiment import *


def launch(args):
    user=  TwitterSentiment(args['<twitter_handle>'],int(args['<number_of_tweets>']))
    
    if args['display_tweets']:
        user.display_tweets()
    elif args['analyse_tweets']:
        user.analyse_data()




if __name__ == '__main__':
    arguments = docopt(__doc__)
    launch(arguments)