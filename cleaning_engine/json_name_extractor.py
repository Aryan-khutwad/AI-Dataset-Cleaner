import ast

def extract_names(df, column):

    def clean_json(text):

        try:
            data = ast.literal_eval(text)

            names = [item['name'] for item in data]

            return ", ".join(names)

        except:
            return text

    df[column] = df[column].astype(str).apply(clean_json)

    return df