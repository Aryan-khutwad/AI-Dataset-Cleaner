def remove_high_missing_columns(df, threshold=0.7):

    missing_percent = df.isnull().mean()

    cols_to_drop = missing_percent[missing_percent > threshold].index

    return df.drop(columns=cols_to_drop)