def standardize_text(df, column):

    df[column] = df[column].astype(str).str.strip().str.title()

    return df