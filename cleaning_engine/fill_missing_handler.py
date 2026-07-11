def fill_missing_values(df, column):

    if df[column].dtype in ['int64', 'float64']:

        df[column] = df[column].fillna(
            df[column].median()
        )

    else:

        df[column] = df[column].fillna(
            df[column].mode()[0]
        )

    return df