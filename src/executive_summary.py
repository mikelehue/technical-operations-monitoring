# Executive summary logic


def generate_executive_summary(
    anomaly_rate,
    maintenance_rate,
    downtime_risk,
    failure_distribution,
    daily_energy,
    alerts_report,
):
    """
    Generate an executive-style summary from operational KPIs and alerts.

    This function is designed as an AI-ready layer: currently deterministic,
    but structured so it can later be replaced or enhanced with an LLM call.
    """

    top_anomaly_machine = anomaly_rate.iloc[0]
    top_maintenance_machine = maintenance_rate.iloc[0]
    top_downtime_machine = downtime_risk.iloc[0]
    most_common_failure = failure_distribution.iloc[1]  # index 0 is usually "Normal"

    total_alerts = len(alerts_report)
    affected_machines = alerts_report["machine_id"].nunique()

    average_daily_energy = daily_energy["average_energy_consumption"].mean()

    summary = f"""
TECHNICAL OPERATIONS EXECUTIVE SUMMARY

The monitoring pipeline processed industrial IoT sensor data and generated operational KPIs, data quality checks, and automated alerts.

Key findings:
- Highest anomaly rate: Machine {int(top_anomaly_machine["machine_id"])} with {top_anomaly_machine["anomaly_rate"]:.2%}.
- Highest maintenance rate: Machine {int(top_maintenance_machine["machine_id"])} with {top_maintenance_machine["maintenance_rate"]:.2%}.
- Highest average downtime risk: Machine {int(top_downtime_machine["machine_id"])} with {top_downtime_machine["average_downtime_risk"]:.2%}.
- Most common non-normal failure type: {most_common_failure["failure_type"]} ({int(most_common_failure["count"])} events).
- Total operational alerts generated: {total_alerts}.
- Machines affected by at least one alert: {affected_machines}.
- Average daily energy consumption: {average_daily_energy:.2f}.

Operational interpretation:
The system identifies a small subset of machines requiring closer monitoring due to elevated anomaly, maintenance, or downtime-risk indicators. These outputs can support preventive maintenance planning, operational prioritization, and technical follow-up.

Recommended next actions:
- Review machines with repeated alerts.
- Investigate dominant failure modes.
- Track whether anomaly rates increase over time.
- Use KPI tables and alert reports as inputs for dashboards or weekly operations reviews.
"""

    return summary.strip()