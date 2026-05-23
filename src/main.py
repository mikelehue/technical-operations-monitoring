# Main pipeline orchestration

from extract import load_raw_data
from transform import clean_data
from load import save_processed_data


def run_pipeline():
    raw_df = load_raw_data()
    clean_df = clean_data(raw_df)
    save_processed_data(clean_df)


if __name__ == "__main__":
    run_pipeline()