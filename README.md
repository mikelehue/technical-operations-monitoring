# Technical Operations Monitoring

A modular ETL, KPI monitoring, and operational alerting pipeline for industrial IoT sensor data.

This project simulates a real-world technical operations workflow where machine sensor data is transformed into operational insights, alerts, and executive reports.

---

## Project Objective

The objective is to identify machines that require attention based on:

- anomaly rates
- maintenance indicators
- downtime risk
- energy consumption patterns

The pipeline is designed to support:

- Technical Operations
- Operations Analytics
- Industrial IoT Monitoring
- Preventive Maintenance
- Operational Reporting

---

## Architecture

```text
Raw Sensor Data
      │
      ▼
Extract
      │
      ▼
Transform
      │
      ▼
Data Quality Checks
      │
      ▼
KPI Generation
      │
      ▼
Alert Generation
      │
      ▼
Executive Summary
```

---

## Dataset

The project uses a Smart Manufacturing / Industrial IoT dataset containing machine-level sensor readings.

Main variables include:

- timestamp
- machine_id
- temperature
- vibration
- humidity
- pressure
- energy_consumption
- machine_status
- anomaly_flag
- failure_type
- downtime_risk
- maintenance_required

---

## Pipeline Components

### Extract
Loads raw sensor data from CSV files.

### Transform
Cleans and enriches the dataset with operational features.

### Data Quality
Validates data integrity through quality checks.

### KPI Generation
Calculates operational metrics such as:

- anomaly rate by machine
- maintenance rate by machine
- average downtime risk
- failure distribution
- daily energy consumption

### Alert Generation
Identifies machines exceeding predefined operational thresholds.

### Executive Summary
Generates a management-oriented summary of the system status.

---

## Outputs

### Processed Data

```text
data/processed/clean_sensor_data.csv
```

### KPI Tables

```text
outputs/tables/
├── anomaly_rate_by_machine.csv
├── maintenance_rate_by_machine.csv
├── average_downtime_risk_by_machine.csv
├── failure_type_distribution.csv
└── daily_energy_consumption.csv
```

### Reports

```text
outputs/reports/
├── alerts_report.csv
└── executive_summary.txt
```

---

## Project Structure

```text
technical-operations-monitoring/
│
├── data/
├── outputs/
├── notebooks/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── data_quality.py
│   ├── kpis.py
│   ├── alerts.py
│   ├── executive_summary.py
│   ├── load.py
│   └── main.py
│
├── README.md
├── requirements.txt
└── config.example.yaml
```

---

## How to Run

```bash
python src/main.py
```

The pipeline automatically:

1. Loads raw data
2. Cleans and transforms records
3. Runs data quality checks
4. Calculates KPIs
5. Generates alerts
6. Produces an executive summary
7. Saves all outputs

---

## Technical Stack

- Python
- Pandas
- CSV-based ETL pipelines
- KPI monitoring
- Operational alerting
- Git / GitHub

---

## About This Project

This project was built as part of a transition toward Technical Operations, Operations Analytics, and Industrial Monitoring roles.

The focus is not pure analytics, but using data to improve operational visibility, prioritization, and decision-making in technical environments.