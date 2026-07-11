def remove_constant_columns(df):

    constant_cols = [col for col in df.columns if df[col].nunique() <= 1]

    return df.drop(columns=constant_cols)