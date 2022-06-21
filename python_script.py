import pandas as pd
import requests, json
from pprint import pprint
import datetime
import numpy as np

# base url for all FPL API endpoints
base_url = 'https://fantasy.premierleague.com/api/'

# get data from bootstrap-static endpoint
r = requests.get(base_url+'bootstrap-static/').json()

teams_info = pd.json_normalize(r['teams'])
teams_info = teams_info.loc[:, (teams_info != teams_info.iloc[0]).any()]
now = datetime.datetime.now()
str_ = str(now.hour) + '_' + str(now.minute) + '_' + str(now.second)
teams_info.rename(columns = {'code':str_}, inplace = True)
teams_info.to_csv('C:/Users/Kishan/cron_scheduling/team_updates.csv')
