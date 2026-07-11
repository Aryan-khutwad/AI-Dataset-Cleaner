def clean_spaces(df, column):

    df[column] = df[column].astype(str).str.strip()

    return df