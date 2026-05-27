# Database loading logic

from pathlib import Path


PROCESSED_DATA_PATH = Path("data/processed/clean_sensor_data.csv")


def save_processed_data(df, output_path=PROCESSED_DATA_PATH):
    """
    Save cleaned sensor data to a processed CSV file.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"Processed data saved to: {output_path}")

KPI_OUTPUT_PATH = Path("outputs/tables")


def save_kpi_table(df, file_name, output_dir=KPI_OUTPUT_PATH):
    """
    Save KPI table to CSV.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / file_name
    df.to_csv(output_path, index=False)
    print(f"KPI table saved to: {output_path}")