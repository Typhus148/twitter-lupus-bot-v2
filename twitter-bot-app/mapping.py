__author__ = 'Shayak', 'Philip'
import vincent
import pandas as pd
from keys import MappingHandlerKeys, CustomColorOptionKeys


def visualizeStateData(stateDict, thresholds, file_name, update):
    statePanda = {}
    stateCount = 0
    # If true means map was updated with new tweet and is to use appropriate color set
    if update:
        color_option = CustomColorOptionKeys.SET_ONE_KEY
    else:
        color_option = CustomColorOptionKeys.PURPLES_KEY

    for (key, value) in stateDict.items():
        statePanda[stateCount] = [key, value]
        stateCount += 1
    stateData = pd.DataFrame.from_dict(statePanda, orient='index')
    stateData.columns = [MappingHandlerKeys.DATA_KEY, MappingHandlerKeys.DATA_BIND_KEY]
    visualizePandasData(stateData, thresholds,
                        file_name, color_option)


# Creates the json file that will be read by the javascript to be displayed on a webpage
def visualizePandasData(stateData, thresholds, file_name, color_option):
    state_topo = 'https://raw.githubusercontent.com/wrobstory/vincent_map_data/master/us_states.topo.json'
    geo_data = [{'name': 'states', 'url': state_topo, 'feature': 'us_states.geo'}]
    vis = vincent.Map(data=stateData, geo_data=geo_data, scale=1000,
                      projection='albersUsa', data_bind=MappingHandlerKeys.DATA_BIND_KEY,
                      data_key=MappingHandlerKeys.DATA_KEY, map_key={'states': 'properties.NAME'}, brew=color_option)
    vis.scales[0].type = 'threshold'
    vis.scales[0].domain = thresholds
    vis.legend(title=MappingHandlerKeys.MAP_TITLE_KEY)
    vis.to_json(file_name)
