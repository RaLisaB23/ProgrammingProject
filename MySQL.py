import mysql.connector
import pandas as pd
from pandas.io import sql
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2o2eP@55w0rd",
  database="drug_connections"
)

rodf = pd.read_json('https://api.sleeper.app/v1/league/918551365406797824/rosters')

# for col in rodf.columns:
#     print(col)

points = []

for data in rodf['settings']:
    points.append(data['ppts'])

rodf2 = rodf[['roster_id', 'owner_id']].copy()
rodf2['Points'] = points

roster = rodf2.copy()

# print(roster)