from application import json
from keys import GeoFileNameKeys, FileNameKeys, JsonKeys, StateKeys
from mapping import visualizeStateData
from twitter_api_geo_update_color_map import updated_state_color


# Saves new geo data for all tweets without a filter option for specific tweets
def save_new_geo_data(state):
    with open(GeoFileNameKeys.GEO_DATA_FILENAME_KEY, 'r') as infile:
        states_tweet_volume = json.load(infile)
    states_tweet_volume[state] += 1

    with open(GeoFileNameKeys.GEO_DATA_FILENAME_KEY, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)
    maximum_tweets(states_tweet_volume, FileNameKeys.TWEET_MAP_KEY)

    # file for html and javascript to read to know if geo_states_data was changed and then to reload tweetMap
    with open(GeoFileNameKeys.GEO_STATES_UPDATE_STATUS_KEY, 'w') as outfile:
        json.dump(JsonKeys.UPDATE_TRUE_KEY, outfile)
    updated_state_color(states_tweet_volume, state)


# Saves new geo data for tweets that are within the filter option
def save_new_geo_options_data(state, filter_option):
    filter_option = filter_option.lower()
    if ' ' in filter_option:
        filter_option.replace(' ', '')
    # This is the json file that stores the counters for each state
    with open(GeoFileNameKeys.GEO_OPTIONAL_FILTER_TWEETS_DIRECTORY_KEY +
              filter_option + GeoFileNameKeys.GEO_DATA_OPTIONAL_FILTER_KEY, 'r') as infile:
        states_tweet_volume = json.load(infile)
    states_tweet_volume[state] += 1

    # writes new geo data for passed option
    with open(GeoFileNameKeys.GEO_OPTIONAL_FILTER_TWEETS_DIRECTORY_KEY +
              filter_option + GeoFileNameKeys.GEO_DATA_OPTIONAL_FILTER_KEY, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)
    maximum_tweets(states_tweet_volume, (GeoFileNameKeys.GEO_OPTIONAL_FILTER_TWEETS_DIRECTORY_KEY + filter_option +
                                         GeoFileNameKeys.GEO_UPDATE_TWEETMAP_KEY))
    updated_state_color(states_tweet_volume, state)


# Used to determine the thresh hold for the tweets to be bucketed in for graphing
def thresh_hold_calculator(max_Tweets):
    thresh_hold = [int(i * max_Tweets / 8) for i in range(0, 8)]
    return thresh_hold


# Gets the highest tweet counter in the state dictionary
def maximum_tweets(states_tweet_volume, file_name):
    max_Tweets = 0
    for state in StateKeys.LIST_STATES_FULL_KEY:
        if states_tweet_volume[state.title()] > max_Tweets:
            max_Tweets = states_tweet_volume[state.title()]
    visualizeStateData(states_tweet_volume, thresh_hold_calculator(max_Tweets), file_name, False)
