def fix_datatypes(df, column):

    try:
        df[column] = df[column].convert_dtypes()
    except:
        pass

    return df