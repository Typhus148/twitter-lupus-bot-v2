import re
from keys import TweetKeywordKeys


# Checks if lupus appears within the text of the tweet
def lupus_text_checker(text):
    word = 'lupus'
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    else:
        return False


# checks for whether some key words are in the tweet's text and if true flags the tweet as not related to lupus
# cleans the api data for irrelevant tweets
def tweet_filter(text):
    word = 'lhandsign'
    for word in TweetKeywordKeys.INVALID_KEYWORDS_KEY:
        if re.search(word, text):
            return True
    if re.search(word, text.lower()):
        return False


# Returns True if the lupus tweet passes both tests to check it pertains to lupus and false if not
def lupus_api_filterer(text):
    if (lupus_text_checker(text['text']) is True) and (tweet_filter(text['text']) is False):
        return True
    else:
        return False
