import polars as pl
from sklearn.linear_model import LinearRegression
import numpy as np
import os

def predict_next_n_days(path: str, n_days: int = 10) -> pl.DataFrame:
    df = pl.read_parquet(path)

    df = df.select(["Date", "Symbol", "AvgPrice"]).with_columns([
        pl.col("Date").cast(pl.Date).alias("ParsedDate")
    ]).drop_nulls()
    print(df)
    results = []

    for symbol in df["Symbol"].unique():
        df_sym = df.filter(pl.col("Symbol") == symbol).sort("ParsedDate")

        x = df_sym["ParsedDate"].cast(pl.Int32).to_numpy().reshape(-1, 1)
        y = df_sym["AvgPrice"].to_numpy()

        if len(x) < 2:
            print(f"[SKIP] Not enough data for {symbol}")
            continue

        model = LinearRegression()
        model.fit(x, y)

        last_day = np.max(x)
        for i in range(1, n_days + 1):
            day = last_day + i
            predicted_price = model.predict([[day]])[0]
            results.append({
                "Symbol": symbol,
                "DayIndex": int(day),
                "DayOffset": i,
                "PredictedPrice": float(predicted_price)
            })

    return pl.DataFrame(results)
