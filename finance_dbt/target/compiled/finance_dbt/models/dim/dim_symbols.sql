SELECT DISTINCT
  Symbol,
  LEFT(Symbol, 4) AS SymbolGroup,
  LENGTH(Symbol) AS SymbolLength
FROM "dev"."main"."stg_stock_prices"