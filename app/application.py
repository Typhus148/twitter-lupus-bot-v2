#!/usr/bin/python3
__author__ = 'Philip'
from app.keys import FileNameKeys, JsonKeys, GeoFileNameKeys, TweetKeywordKeys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
# from twitter_api_filterer import lupus_api_filterer
# from twitter_api_util import save_new_geo_data, GEO_STATES_UPDATE_STATUS
import json
# from twitter_api_states import api_states
# from twitter_api_additional_map_filters import update_geo_option_data


class StdOutListener(StreamListener):
    def on_data(self, data):
        with open(FileNameKeys.FETCHED_TWEETS_KEY, 'a') as tf:
            # Check to make sure data is not null and can be loaded from json to text
            if data:
                text = json.loads(data)
                # filters tweets before storing them to see if they are related to lupus -WIP
                if lupus_api_filterer(text):
                    # checks if the tweet has any valid geo data otherwise skips updating the json file
                    state = api_states(text)
                    if state is False:
                        with open(GeoFileNameKeys.GEO_STATES_UPDATE_STATUS_KEY, 'r') as update_status_infile:
                            status_check = json.load(update_status_infile)
                        if status_check[JsonKeys.STATUS_KEY]:
                            update_status = {"status": False}
                            with open(GeoFileNameKeys.GEO_STATES_UPDATE_STATUS_KEY, 'w') as update_status_outfile:
                                json.dump(update_status, update_status_outfile)
                    else:
                        # Updates geo data if there was a update to the geo data counter
                        save_new_geo_data(state)
                        update_geo_option_data(text, state)

                    # Appends the new tweet to the list of previous tweets
                    tf.write(data)
                    # Prints the tweet into the console for visual observance of tweet coming in
                    # print('@%s : %s\n' % (text[JsonKeys.USER_KEY][JsonKeys.SCREEN_NAME_KEY], text[JsonKeys.TEXT_KEY]))
                    return True

    def on_error(self, status):
        print(status)


def lupus_tweet_tracker_setup():
    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(TwitterApiAuthKeys.CONSUMER_KEY, TwitterApiAuthKeys.CONSUMER_SECRET_KEY)
    auth.set_access_token(TwitterApiAuthKeys.ACCESS_TOKEN_KEY, TwitterApiAuthKeys.ACCESS_TOKEN_SECRET_KEY)
    stream = Stream(auth, l)

    stream.filter(track=TweetKeywordKeys.LUPUS_KEYWORDS_KEY)


if __name__ == '__main__':
    lupus_tweet_tracker_setup()
