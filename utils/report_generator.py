def generate_report(original_df, cleaned_df):

    report = {
        "Original Rows": original_df.shape[0],
        "Cleaned Rows": cleaned_df.shape[0],
        "Original Columns": original_df.shape[1],
        "Cleaned Columns": cleaned_df.shape[1],
        "Rows Removed": original_df.shape[0] - cleaned_df.shape[0],
        "Columns Removed": original_df.shape[1] - cleaned_df.shape[1]
    }

    return report