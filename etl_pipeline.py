import duckdb

def query_duckdb( db_path="data/warehouse/finance.duckdb"):
    con = duckdb.connect(db_path)
    df=con.execute("SELECT * FROM stocks").df()
    print(df)
    return f"Loaded  into DuckDB."
query_duckdb()