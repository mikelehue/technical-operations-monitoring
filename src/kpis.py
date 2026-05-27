# KPI calculation functions

def calculate_anomaly_rate_by_machine(df):
    return (
        df.groupby("machine_id")["anomaly_flag"]
        .mean()
        .reset_index(name="anomaly_rate")
        .sort_values("anomaly_rate", ascending=False)
    )


def calculate_maintenance_rate_by_machine(df):
    return (
        df.groupby("machine_id")["maintenance_required"]
        .mean()
        .reset_index(name="maintenance_rate")
        .sort_values("maintenance_rate", ascending=False)
    )


def calculate_average_downtime_risk_by_machine(df):
    return (
        df.groupby("machine_id")["downtime_risk"]
        .mean()
        .reset_index(name="average_downtime_risk")
        .sort_values("average_downtime_risk", ascending=False)
    )


def calculate_failure_type_distribution(df):
    return (
        df["failure_type"]
        .value_counts()
        .reset_index(name="count")
        .rename(columns={"failure_type": "failure_type"})
    )


def calculate_daily_energy_consumption(df):
    return (
        df.groupby("date")["energy_consumption"]
        .mean()
        .reset_index(name="average_energy_consumption")
        .sort_values("date")
    )