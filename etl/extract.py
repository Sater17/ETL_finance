import yfinance as yf
from datetime import date
import polars as pl

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "BRK-B", "UNH", "V"]

start_date = "2023-12-26"
end_date = "2024-01-06"

def extract_data():
    df = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        interval="1d",
        group_by="ticker",
        auto_adjust=False,
        threads=True)
    df.reset_index(inplace=True)
    pl_df = pl.DataFrame(df)
    pl_df.write_parquet(f"data/raw/{date.today()}.parquet")
    print (df.columns)
    return f"data/raw/{date.today()}.parquet"
