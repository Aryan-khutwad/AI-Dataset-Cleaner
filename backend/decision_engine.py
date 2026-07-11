import pandas as pd


def detect_column_type(df, column):

    series = df[column]

    if pd.api.types.is_numeric_dtype(series):
        return "numeric"

    # if pd.api.types.is_object_dtype(series):

    #     sample = series.dropna().astype(str)

    #     if len(sample) == 0:
    #         return "unknown"

    #     sample_text = " ".join(sample.head(5))

    #     if "[{" in sample_text and "name" in sample_text:
    #         return "json"

    #     return "text"
    if pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series):

        sample = series.dropna().astype(str)

        if len(sample) == 0:
            return "unknown"

        sample_text = " ".join(sample.head(5))

        if "[{" in sample_text and "name" in sample_text:
            return "json"

        return "text"

    return "unknown"


def get_missing_percentage(df, column):

    return df[column].isnull().mean()


def should_fill_missing(df, column):

    missing_percent = get_missing_percentage(df, column)

    return 0 < missing_percent <= 0.4


def should_remove_null_rows(df, column):

    missing_percent = get_missing_percentage(df, column)

    return 0.4 < missing_percent <= 0.7