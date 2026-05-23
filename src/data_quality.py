# Data quality validation checks
import pandas as pd

def run_data_quality_checks(df):
    print("DATA QUALITY REPORT")
    print("-------------------")

    print(f"Rows processed: {len(df)}")

    missing_values = df.isnull().sum().sum()
    print(f"Missing values: {missing_values}")

    duplicate_rows = df.duplicated().sum()
    print(f"Duplicate rows: {duplicate_rows}")

    duplicate_machine_timestamps = df.duplicated(
        subset=["machine_id", "timestamp"]
    ).sum()
    print(f"Duplicate machine/timestamp records: {duplicate_machine_timestamps}")

    invalid_anomaly_flags = ~df["anomaly_flag"].isin([0, 1])
    print(f"Invalid anomaly flags: {invalid_anomaly_flags.sum()}")

    invalid_maintenance_flags = ~df["maintenance_required"].isin([0, 1])
    print(f"Invalid maintenance flags: {invalid_maintenance_flags.sum()}")

    invalid_machine_status = ~df["machine_status"].isin([0, 1, 2])
    print(f"Invalid machine status values: {invalid_machine_status.sum()}")

    anomalies_by_machine = df.groupby("machine_id")["anomaly_flag"].sum()
    high_anomaly_machines = anomalies_by_machine[anomalies_by_machine > 200]

    print(f"Machines above anomaly threshold: {len(high_anomaly_machines)}")