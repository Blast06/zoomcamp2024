
import sys
import pandas as pd
from sqlalchemy import create_engine
from time import time
from pip import _internal

_internal.main(['list'])

nyc_taxis = pd.read_csv("2_docker_sql\green_tripdata_2021-01.csv", nrows=100)


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# nyc_taxis.head()



# nyc_taxis.tpep_pickup_datetime = pd.to_datetime(nyc_taxis.tpep_pickup_datetime)
# nyc_taxis.tpep_dropoff_datetime = pd.to_datetime(nyc_taxis.tpep_dropoff_datetime)
# taxi_zones = pd.read_csv("2_docker\zone_loookup.csv")

# print(pd.io.sql.get_schema(nyc_taxis, name='yellow_taxi_data'))


#df_iter = pd.read_csv('2_docker_sql\yellow_tripdata_2021-01.csv', iterator= True, chunksize=100000)


# nyc_taxis = next(df_iter)



# nyc_taxis.tpep_pickup_datetime = pd.to_datetime(nyc_taxis.tpep_pickup_datetime)
# nyc_taxis.tpep_dropoff_datetime = pd.to_datetime(nyc_taxis.tpep_dropoff_datetime)



# nyc_taxis.head.to_sql('green_taxi_data', con=engine, if_exists='replace')
# taxi_zones.to_sql('zones', con=engine, if_exists='replace')



  