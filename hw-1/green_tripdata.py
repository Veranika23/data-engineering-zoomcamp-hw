import duckdb
import numpy as np
import pandas as pd 

# Question 3
q3_result = duckdb.query("SELECT count(*) as short_trips FROM 'green_tripdata_2025-11.parquet' where (lpep_pickup_datetime >= '2025-11-01' and lpep_pickup_datetime < '2025-12-01') and trip_distance <= 1").to_df()
print(q3_result)

#Question 4
q4_result = duckdb.query("SELECT lpep_pickup_datetime FROM 'green_tripdata_2025-11.parquet' where trip_distance = (select max(trip_distance) from 'green_tripdata_2025-11.parquet' where trip_distance < 100)").to_df()
print(q4_result)

#Question 5
q5_result = duckdb.query("SELECT loc.Zone, sum(total_amount) as total_amount from 'green_tripdata_2025-11.parquet' trip left join 'taxi_zone_lookup.csv' loc on trip.PUlocationID = loc.LocationID where DATE(lpep_pickup_datetime) = '2025-11-18' group by loc.Zone order by total_amount desc limit 1").to_df()
print(q5_result)

# df = pd.read_parquet('green_tripdata_2025-11.parquet')
# print(list(df.columns))

# df = pd.read_csv('taxi_zone_lookup.csv')
# print(list(df.columns))

#Question 6
q6_result = duckdb.query("SELECT locDO.Zone as dropoff_zone, tip_amount  from 'green_tripdata_2025-11.parquet' trip left join 'taxi_zone_lookup.csv' locPU on trip.PUlocationID = locPU.LocationID left join 'taxi_zone_lookup.csv' locDO on trip.DOLocationID = locDO.LocationID where (DATE(lpep_pickup_datetime) >= '2025-11-01' and  DATE(lpep_pickup_datetime) < '2025-12-01') and locPU.Zone = 'East Harlem North' order by tip_amount desc limit 1")
print(q6_result)