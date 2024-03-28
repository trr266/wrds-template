import wrds
import pandas as pd
import duckdb
import os


table_name = 'bank_fundq'

# Fetch data from WRDS
os.environ["PGPASSWORD"] = os.environ.get('WRDS_PASSWORD')
os.environ["PGUSER"] = os.environ.get('WRDS_USERNAME')
db = wrds.Connection()
data = db.get_table(library='comp', table = table_name, obs=10)

# Load data into a pandas DataFrame
df = pd.DataFrame(data)

# Initialize a DuckDB connection
duckdb_conn = duckdb.connect()

# Load the DataFrame into a DuckDB table
duckdb_conn.from_df(df, table_name)
#duckdb.register(table_name, df)
duckdb_conn.sql(f"CREATE TABLE {table_name} AS SELECT * FROM df")

# Save the DuckDB table to a Parquet file
duckdb_conn.sql(f"COPY {table_name} TO '{table_name}.parquet' (FORMAT 'PARQUET')")