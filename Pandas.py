import pandas as pd
#from sqlalchemy import create_engine


drugs = "C:/Users/12102/Downloads/Drugs.csv"
index = "C:/Users/12102/Downloads/Index.csv"
condition = "C:/Users/12102/Downloads/Conditions.csv"

df_drugs = pd.read_csv(drugs)
df_index = pd.read_csv(index)
df_conditions = pd.read_csv(condition)

df_drugs = df_drugs.set_index(['urlDrugName'])
#df_index = df_index.set_index(['index'])
df_conditions = df_conditions.set_index(['condition'])

drug_index = pd.merge(df_index, df_drugs, how = 'inner')
drug_conditions = pd.merge(drug_index, df_conditions, how = 'inner')
drug_conditions
print(drug_conditions.to_string())

#drug_connections = pd.merge(df_drugs, df_index, left_index=True, right_index=True)
#drug_connections = pd.merge(btc, eth, left_index=True, right_index=True)

engine = create_engine('mysql+mysqlconnector://root:2o2eP@55w0rd@localhost/index')
drug_connections.to_sql(name = 'index', con=engine, if_exists='replace')

try:
    query = "SELECT * FROM tablename WHERE BTC_open <= 30000;"
    resuts = pd.read_sql_query(query, con=engine)
    print(result)
finally:
    mydb.close()