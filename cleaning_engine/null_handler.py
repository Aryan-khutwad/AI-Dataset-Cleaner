def remove_nulls(df, column):

    return df[df[column].notnull()]