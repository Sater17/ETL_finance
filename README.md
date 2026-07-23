# 📈 ETL Finance Pipeline

An end-to-end ETL pipeline that extracts financial market data, transforms it into an analytics-ready format, and loads it into a data warehouse for reporting and visualization.

## 🚀 Project Overview

This project demonstrates how to build a modern data engineering pipeline for financial data.

The pipeline automates the following workflow:

```
Financial API
      │
      ▼
Extract
      │
      ▼
Transform (Cleaning, Validation, Feature Engineering)
      │
      ▼
Load (DuckDB / BigQuery / PostgreSQL)
      │
      ▼
Dashboard / Analytics
```

## ✨ Features

- Automated financial data extraction
- Incremental ETL pipeline
- Data cleaning and validation
- Feature engineering
- Modular project structure
- Configurable through environment variables
- Ready for scheduling with Prefect / Airflow
- Dashboard-ready datasets

---

## 🛠 Tech Stack

- Python
- Polars / Pandas
- DuckDB
- SQL
- Dagster
---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Sater17/ETL_finance.git
cd ETL_finance
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run Pipeline

Run the complete ETL pipeline

```bash
python main.py
```

Or execute each stage individually

```bash
python src/extract/extract.py

python src/transform/transform.py

python src/load/load.py
```

---

## 📊 Data Pipeline

1. Extract financial data from API
2. Store raw data
3. Clean missing values
4. Normalize schema
5. Generate analytical metrics
6. Load into data warehouse
7. Visualize using BI dashboard


## 🧪 Future Improvements

- Add Airflow orchestration
- CI/CD with GitHub Actions
- Unit testing
- Docker deployment
- Data quality checks
- Incremental loading
- Real-time streaming pipeline

---

## 📄 License

This project is intended for educational and portfolio purposes.
