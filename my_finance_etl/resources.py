from dagster_dbt import dbt_cli_resource
from pathlib import Path

dbt_resource = dbt_cli_resource.configured({
    "project_dir": str(Path("finance_dbt").resolve()),  # đường dẫn tới thư mục dbt
})
