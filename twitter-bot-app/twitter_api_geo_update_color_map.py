from mapping import visualizeStateData
from keys import FileNameKeys, StateKeys


# Used to determine the thresh hold for the tweets to be bucketed in for graphing
def thresh_hold_calculator(max_Tweets):
    thresh_hold = [int(i * max_Tweets / 8) for i in range(0, 8)]
    thresh_hold[7] = int(max_Tweets * 2)
    return thresh_hold


# Gets the highest tweet counter in the state dictionary
def updated_maximum_tweets(states_tweet_volume):
    max_Tweets = 0
    for state in StateKeys.LIST_STATES_FULL_KEY:
        if states_tweet_volume[state.title()] > max_Tweets:
            max_Tweets = states_tweet_volume[state.title()]
    return max_Tweets


# Changes the value of the state given which has just been updated
def updated_state_color(states_tweet_volume, state_update):
    max_Tweets = updated_maximum_tweets(states_tweet_volume)
    states_tweet_volume[state_update] = max_Tweets * 2
    visualizeStateData(states_tweet_volume, thresh_hold_calculator(max_Tweets),
                       FileNameKeys.WEBPAGE_UPDATE_TWEETMAP_KEY, True)
