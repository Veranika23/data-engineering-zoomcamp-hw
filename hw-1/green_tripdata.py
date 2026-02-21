import duckdb
import numpy as np
import pandas as pd 

# Question 3
result = duckdb.query("SELECT count(*) as short_trips FROM 'green_tripdata_2025-11.parquet' where (lpep_pickup_datetime >= '2025-11-01' and lpep_pickup_datetime < '2025-12-01') and trip_distance <= 1").to_df()
print(result)

#Question 4

