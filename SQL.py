import mysql.connector
import pandas as pd
from pandas.io import sql
import json
'''
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

'''
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Pa55w0rd",
    database = "drug_conditions"
)

usdf = pd.read_json('https://api.sleeper.app/v1/league/918551365406797824/users')

usdf2 = usdf[['', '']].copy()

user = usdf2.copy()

# print(user)


