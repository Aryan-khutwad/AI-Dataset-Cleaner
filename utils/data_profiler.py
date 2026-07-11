def profile_data(df):

    profile = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum(),
        "Memory Usage (KB)": round(df.memory_usage(deep=True).sum() / 1024, 2)
    }

    return profile

def column_profile(df):

    column_info = []

    for col in df.columns:

        info = {
            "Column": col,
            "Datatype": str(df[col].dtype),
            "Missing Values": df[col].isnull().sum(),
            "Unique Values": df[col].nunique()
        }

        column_info.append(info)

    return column_info