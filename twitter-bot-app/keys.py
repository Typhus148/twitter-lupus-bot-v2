__author__ = 'Philip'


class TweetKeywordKeys:
    LUPUS_KEYWORDS_KEY = ['lupus', '#lupusawarenessmonth', '#lupus', 'lupusawarenessmonth', 'lupus awareness month',
                          '#TEAMLUPUS', '#beatlupus', 'lhandsign', '#lhandsign', '#lupusawareness',
                          'lupusawareness', 'lupus awareness']
    INVALID_KEYWORDS_KEY = ['canis', 'homini', 'wolf', 'wolves']


class AdditionalFilterOptionKeys:
    FILTER_OPTIONS_KEY = ['lupus', 'lupusawarenessmonth', 'lupus awareness month', '#TEAMLUPUS',
                          '#beatlupus', 'lhandsign']


class JsonKeys:
    TEXT_KEY = 'text'
    USER_KEY = 'user'
    SCREEN_NAME_KEY = 'screen_name'
    STATUS_KEY = 'status'
    UPDATE_TRUE_KEY = {"status": True}
    UPDATE_FALSE_KEY = {"status": False}
    LOCATION_KEY = 'location'


class TwitterApiAuthKeys:
    ACCESS_TOKEN_KEY = '737646162820399104-MFFoB4Q0GkY6W9PCZRv51MzXWaHoOvN'
    ACCESS_TOKEN_SECRET_KEY = 'rR2Kd80DJbDYJFJlBJcjZLMrsn6Z7qemks40Zrz8In2EC'
    CONSUMER_KEY = 'VFUVMZ3MLPNvWRnvLcJGV3qzc'
    CONSUMER_SECRET_KEY = '1ZFOZbL5lKtQBfI0ad2rjlQlnDIrwegHeWnSMzeFygkbogjJaC'


class GeoFileNameKeys:
    GEO_DATA_FILENAME_KEY = 'geo_data_states.json'
    GEO_STATES_UPDATE_STATUS_KEY = 'geo_data_states_update_status.json'
    GEO_OPTIONAL_FILTER_TWEETS_DIRECTORY_KEY = 'Geo_data_optional_tweet_filters/'
    GEO_UPDATE_TWEETMAP_KEY = '_tweetMap.json'
    GEO_DATA_OPTIONAL_FILTER_KEY = '_map_filter_options.json'


class StateKeys:
    VIRGINIA_KEY = 'Virginia'
    PENNSYLVANIA_KEY = 'Pennsylvania'
    LIST_STATES_FULL_KEY = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut',
                            'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa',
                            'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan',
                            'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire',
                            'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio',
                            'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota',
                            'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia',
                            'wisconsin', 'wyoming']
    LIST_STATES_PLAIN_KEY = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA',
                             'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                             'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT',
                             'VA', 'WA', 'WV', 'WI', 'WY']
    LIST_STATES_KEY = ['\bAL\b', '\bAK\b', '\bAZ\b', '\bAR\b', '\bCA\b', '\bCO\b', '\bCT\b', '\bDE\b', '\bFL\b',
                       '\bGA\b', '\bHI\b', '\bID\b', '\bIL\b', '\bIN\b', '\bIA\b', '\bKS\b', '\bKY\b', '\bLA\b',
                       '\bME\b', '\bMD\b', '\bMA\b', '\bMI\b', '\bMN\b', '\bMS\b', '\bMO\b', '\bMT\b', '\bNE\b',
                       '\bNV\b', '\bNH\b', '\bNJ\b', '\bNM\b', '\bNY\b', '\bNC\b', '\bND\b', '\bOH\b', '\bOK\b',
                       '\bOR\b', '\bPA\b', '\bRI\b', '\bSC\b', '\bSD\b', '\bTN\b', '\bTX\b', '\bUT\b', '\bVT\b',
                       '\bVA\b', '\bWA\b', '\bWV\b', '\bWI\b', '\bWY\b']


class MappingHandlerKeys:
    DATA_BIND_KEY = 'tweets'
    DATA_KEY = 'states'
    MAP_TITLE_KEY = '# of Lupus Tweets'


class FileNameKeys:
    FETCHED_TWEETS_KEY = 'fetched_lupus_tweets.txt'
    TWEET_MAP_KEY = 'tweetMap.json'
    WEBPAGE_UPDATE_TWEETMAP_KEY = 'update_tweetMap.json'


class CustomColorOptionKeys:
    SET_ONE_KEY = 'Custom_set_1'
    PURPLES_KEY = 'Purples'
