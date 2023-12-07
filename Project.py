import pandas as pd
import mysql.connector
from sqlalchemy import create_engine



eth = eth.set_index(['ETH_time'])

#merging the 2 pandas
new_frame = pd.merge(btc, eth, left_index=True, right_index=True)
engine = create_engine('mysql+mysqlconnector://root:2o2eP@55w0rd@localhost/dfname')
new_frame.to_sql(name = 'dfname', con=engine, if_exists='replace')

try:
    query = "SELECT * FROM tablename WHERE BTC_open <= 30000;"
    resuts = pd.read_sql_query(query, con=engine)
    print(result)
finally:
    mydb.close()