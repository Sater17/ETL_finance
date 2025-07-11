import polars as pl
import ast  # dùng để parse string thành tuple an toàn
import os

def melt_stock_data(path : str)-> str:
    df = pl.read_parquet(path)
    
    df = df.rename({
        col: "_".join(filter(None,ast.literal_eval(col))) if col.startswith("(") else col
        for col in df.columns
    })
    symbols = set()
    for col in df.columns:
        if "_" in col:
            symbol,_ = col.split("_")
            symbols.add(symbol)
            
    dfs=[]
    for symbol in symbols:
        try:
            df_symbol = df.select([
                pl.col("Date"),
                pl.col(f"{symbol}_Open").alias("Open"),
                pl.col(f"{symbol}_High").alias("High"),
                pl.col(f"{symbol}_Low").alias("Low"),
                pl.col(f"{symbol}_Close").alias("Close"),
                pl.col(f"{symbol}_Volume").alias("Volume"),
            ]).with_columns([
                pl.lit(symbol).alias("Symbol")
            ])
            dfs.append(df_symbol)
        except pl.exceptions.ColumnNotFoundError:
            print(f"[WARN] Missing column for symbol: {symbol}, skipping.")
    if dfs:
        long_df = pl.concat(dfs)
    else:
        raise ValueError("❌ Không có symbol nào hợp lệ để xử lý (dfs rỗng).")
    long_df = pl.concat(dfs)
    
    long_df = long_df.sort(["Symbol", "Date"]).with_columns([
        ((pl.col("High") + pl.col("Low")) / 2).alias("AvgPrice"),
        (pl.col("Close").pct_change().over("Symbol").fill_null(0)).alias("PctChange")
    ])
    out_path = path.replace("raw", "processed")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    long_df.write_parquet(out_path)
    print(f"✅ Transformed file saved to: {out_path}")

    return out_path
