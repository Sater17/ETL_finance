# my_finance_etl/jobs.py
from dagster import job, op
from etl.extract import extract_data
from etl.transform import melt_stock_data
from etl.load import load_to_duckdb
from etl.predict import predict_next_n_days
import os
from dagster_dbt import dbt_cli_resource
from my_finance_etl.resources import dbt_resource

@op
def extract_op():
    return extract_data()

@op
def transform_op(raw_path: str):
    return melt_stock_data(raw_path)

@op
def load_op(processed_path: str):
    return load_to_duckdb(processed_path)

@op
def predict_op(processed_path: str) -> str:
    pred_df = predict_next_n_days(processed_path)
    out_path = processed_path.replace("processed", "predicted").replace(".parquet", "_predict.parquet")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    pred_df.write_parquet(out_path)
    return out_path

@op(required_resource_keys={"dbt"})
def run_dbt_op(context):
    result = context.resources.dbt.run(["--vars", '{data_path: "file:///C:/Users/SATER/Projects/tmp/data/processed/2025-07-10.parquet"}'])
    # for event in result:
    #     context.log.info(event)

@job(resource_defs={"dbt": dbt_resource})
def finance_etl_job():
    raw = extract_op()                  # -> str path
    processed = transform_op(raw)      # -> str path
    load_op(processed)
    predict_op(processed) 
    run_dbt_op()
