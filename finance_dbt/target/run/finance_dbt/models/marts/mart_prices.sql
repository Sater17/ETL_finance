
  
    
    

    create  table
      "dev"."main"."mart_prices__dbt_tmp"
  
    as (
      SELECT 
  s.Date,
  s.Symbol,
  s.Close,
  s.PctChange,
  s.AvgPrice,
  d.SymbolGroup
FROM "dev"."main"."stg_stock_prices" s
JOIN "dev"."main"."dim_symbols" d
  ON s.Symbol = d.Symbol
    );
  
  