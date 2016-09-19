import re
from keys import StateKeys


# Checks whether location or coordinate field is null or not
def null_checker(text):
    if text is None:
        return True
    else:
        return False


# Changed return True to return the state that was tagged
# checks for state abbreviation in location key
def location_abbreviation_check(text):
    i = 0
    if len(text) == 2:
        for state in StateKeys.LIST_STATES_PLAIN_KEY:
            match = re.search(state, text)
            if match:
                state_key = StateKeys.LIST_STATES_FULL_KEY[i]
                return state_key.title()
            else:
                i += 1
    else:
        for state in StateKeys.LIST_STATES_KEY:
            match = re.search(state, text)
            if match:
                state_key = StateKeys.LIST_STATES_FULL_KEY[i]
                return state_key.title()
            else:
                i += 1
    return False


# Changed return True to return the state that was tagged
# checks for state in location key if not abbreviated
def location_verify(text):
    text = text.lower()
    i = 0
    w1 = 'washington dc'
    w2 = 'washington, dc'
    w3 = 'washington d.c.'
    w4 = 'washington, pa'
    w5 = 'washington pa'
    match1 = re.search(w1, text)
    match2 = re.search(w2, text)
    match3 = re.search(w3, text)
    match4 = re.search(w4, text)
    match5 = re.search(w5, text)
    if match1:
        return StateKeys.VIRGINIA_KEY
    if match2:
        return StateKeys.VIRGINIA_KEY
    if match3:
        return StateKeys.VIRGINIA_KEY
    if match4:
        return StateKeys.PENNSYLVANIA_KEY
    if match5:
        return StateKeys.PENNSYLVANIA_KEY
    for state in StateKeys.LIST_STATES_FULL_KEY:
        match = re.search(state, text)
        if match:
            return state.title()
        else:
            i += 1
    return False


# Function to be called to check a tweet for location information and add it to the map/graph
def api_states(tweet_LG):
    if tweet_LG['user']['location']:
        state_var1 = location_verify(tweet_LG['user']['location'])
        state_var2 = location_abbreviation_check(tweet_LG['user']['location'])
        # if no valid state from searching for full state names check for abbreviations
        if location_verify(tweet_LG['user']['location']) is False:
            # if abbreviation returns false then it will return the state abbreviated in tweet
            if location_abbreviation_check(tweet_LG['user']['location']) is False:
                return False
            return state_var2
        return state_var1
    return False
