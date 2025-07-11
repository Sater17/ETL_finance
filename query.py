import duckdb

con = duckdb.connect("C:/Users/SATER/Projects/tmp/data/warehouse/finance.duckdb")

# Xem bảng có trong DuckDB
print(con.execute("SELECT schema_name FROM information_schema.schemata").fetchall())

# Query dữ liệu bảng
df = con.execute("SELECT * FROM main.mart_prices LIMIT 10").df()
print(df)
