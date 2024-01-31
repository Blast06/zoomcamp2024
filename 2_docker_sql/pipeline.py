import sys
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

#SET DATABASE CONNECTION



# some fancy stuff with pandas jejeje like loading csv file


nyc_taxis = pd.read_csv("/app/yellow_tripdata_2021-01.csv",low_memory=False)

# engine = create_engine('postgresql://root:root@0.0.0.0/ny_taxi')
engine = create_engine('postgresql://root:root@{}:5432/database'.format('db'))
engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")
conn_url = 'postgresql+psycopg2://root:root@2_docker_sql-db-1/ny_taxi'
engine = create_engine(conn_url)
# db_URL = f"postgresql+psycopg2://{root}:{root}@db:5432/ny_taxi"
#preview first 5 rows
# engine = create_engine(db_URL)
print(nyc_taxis.head())

#insert into the database 

nyc_taxis.to_sql('ny_taxi', con= engine, if_exists='append', index=False)

print('Job finished succesfully for day')