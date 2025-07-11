import duckdb

def load_to_duckdb(path: str, db_path="data/warehouse/finance.duckdb"):
    con = duckdb.connect(db_path)
    con.execute("CREATE TABLE IF NOT EXISTS stocks AS SELECT * FROM read_parquet(?)", [path])
    return f"Loaded {path} into DuckDB."