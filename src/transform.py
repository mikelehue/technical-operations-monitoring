# Data cleaning and transformation logic
import pandas as pd


def clean_data(df):
    """
    Clean and prepare raw sensor data for operational monitoring.
    """
    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.day_name()

    df = df.sort_values(["machine_id", "timestamp"])

    return df