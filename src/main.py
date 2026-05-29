# Main pipeline orchestration

from extract import load_raw_data
from transform import clean_data
from data_quality import run_data_quality_checks
from load import save_processed_data, save_kpi_table, save_report_table, save_text_report
from alerts import generate_alerts
from executive_summary import generate_executive_summary

from kpis import (
    calculate_anomaly_rate_by_machine,
    calculate_maintenance_rate_by_machine,
    calculate_average_downtime_risk_by_machine,
    calculate_failure_type_distribution,
    calculate_daily_energy_consumption,
)


def run_pipeline():

    raw_df = load_raw_data()

    clean_df = clean_data(raw_df)

    run_data_quality_checks(clean_df)

    anomaly_rate = calculate_anomaly_rate_by_machine(clean_df)

    maintenance_rate = calculate_maintenance_rate_by_machine(clean_df)

    downtime_risk = calculate_average_downtime_risk_by_machine(clean_df)

    failure_distribution = calculate_failure_type_distribution(clean_df)

    daily_energy = calculate_daily_energy_consumption(clean_df)

    save_kpi_table(anomaly_rate, "anomaly_rate_by_machine.csv")
    
    save_kpi_table(maintenance_rate, "maintenance_rate_by_machine.csv")
    
    save_kpi_table(downtime_risk, "average_downtime_risk_by_machine.csv")
    
    save_kpi_table(failure_distribution, "failure_type_distribution.csv")
    
    save_kpi_table(daily_energy, "daily_energy_consumption.csv")

    print(anomaly_rate.head())

    print(maintenance_rate.head())

    print(downtime_risk.head())

    print(failure_distribution.head())

    print(daily_energy.head())

    save_processed_data(clean_df)

    alerts_report = generate_alerts(anomaly_rate, maintenance_rate, downtime_risk)
    
    save_report_table(alerts_report, "alerts_report.csv")

    executive_summary = generate_executive_summary(
        anomaly_rate,
        maintenance_rate,
        downtime_risk,
        failure_distribution,
        daily_energy,
        alerts_report,
    )

    save_text_report(
        executive_summary,
        "executive_summary.txt"
    )


if __name__ == "__main__":

    run_pipeline()