SELECT 
  s.Date,
  s.Symbol,
  s.Close,
  s.PctChange,
  s.AvgPrice,
  d.SymbolGroup
FROM {{ ref('stg_stock_prices') }} s
JOIN {{ ref('dim_symbols') }} d
  ON s.Symbol = d.Symbol
