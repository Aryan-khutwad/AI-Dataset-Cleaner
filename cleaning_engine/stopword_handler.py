from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def remove_stopwords(df, column):

    def clean_text(text):

        words = str(text).split()

        filtered_words = [
            word for word in words
            if word.lower() not in ENGLISH_STOP_WORDS
        ]

        return " ".join(filtered_words)

    df[column] = df[column].apply(clean_text)

    return df