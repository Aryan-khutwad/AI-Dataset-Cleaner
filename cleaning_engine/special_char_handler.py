def remove_special_characters(df, column):

    df[column] = df[column].astype(str).str.replace(
        r'[^a-zA-Z0-9 ]',
        '',
        regex=True
    )

    return df