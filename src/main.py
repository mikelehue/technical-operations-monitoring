# Main pipeline orchestration

from extract import load_raw_data
from transform import clean_data
from data_quality import run_data_quality_checks
from load import save_processed_data


def run_pipeline():
    raw_df = load_raw_data()
    clean_df = clean_data(raw_df)

    run_data_quality_checks(clean_df)

    save_processed_data(clean_df)


if __name__ == "__main__":
    run_pipeline()