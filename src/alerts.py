# Operational alert generation logic

import pandas as pd


def generate_alerts(
    anomaly_rate,
    maintenance_rate,
    downtime_risk,
    anomaly_threshold=0.10,
    maintenance_threshold=0.20,
    downtime_threshold=0.09,
):
    """
    Generate operational alerts based on KPI thresholds.
    """
    alerts = []

    high_anomaly = anomaly_rate[anomaly_rate["anomaly_rate"] > anomaly_threshold]

    for _, row in high_anomaly.iterrows():
        alerts.append({
            "machine_id": row["machine_id"],
            "alert_type": "High anomaly rate",
            "metric_value": row["anomaly_rate"],
            "threshold": anomaly_threshold,
        })

    high_maintenance = maintenance_rate[
        maintenance_rate["maintenance_rate"] > maintenance_threshold
    ]

    for _, row in high_maintenance.iterrows():
        alerts.append({
            "machine_id": row["machine_id"],
            "alert_type": "High maintenance rate",
            "metric_value": row["maintenance_rate"],
            "threshold": maintenance_threshold,
        })

    high_downtime = downtime_risk[
        downtime_risk["average_downtime_risk"] > downtime_threshold
    ]

    for _, row in high_downtime.iterrows():
        alerts.append({
            "machine_id": row["machine_id"],
            "alert_type": "High downtime risk",
            "metric_value": row["average_downtime_risk"],
            "threshold": downtime_threshold,
        })

    return pd.DataFrame(alerts)