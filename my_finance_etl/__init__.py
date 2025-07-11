from dagster import Definitions
from .jobs import finance_etl_job
from .schedules import daily_finance_etl_schedule

defs = Definitions(
    jobs=[finance_etl_job],
    schedules=[daily_finance_etl_schedule], 
)