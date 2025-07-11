# my_finance_etl/schedules.py

from dagster import ScheduleDefinition
from .jobs import finance_etl_job

daily_finance_etl_schedule = ScheduleDefinition(
    job=finance_etl_job,
    cron_schedule="45 23 * * *",             # 7h sáng theo giờ Asia/Bangkok
    execution_timezone="Asia/Bangkok"
)
