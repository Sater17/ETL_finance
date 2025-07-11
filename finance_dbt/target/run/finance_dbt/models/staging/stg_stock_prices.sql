
  
    
    

    create  table
      "dev"."main"."stg_stock_prices__dbt_tmp"
  
    as (
      with source as (
    select * from read_parquet('../data/processed/2025-07-10.parquet')
    -- select * from read_parquet('data\processed\2025-07-10.parquet')
)

select
    Symbol,
    Date,
    Open,
    High,
    Low,
    Close,
    Volume,
    AvgPrice,
    PctChange
from source
    );
  
  