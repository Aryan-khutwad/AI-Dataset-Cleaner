from cleaning_engine.null_handler import remove_nulls
from cleaning_engine.duplicate_handler import remove_duplicates
from cleaning_engine.empty_column_handler import remove_empty_columns
from cleaning_engine.datatype_handler import fix_datatypes
from cleaning_engine.fill_missing_handler import fill_missing_values
from cleaning_engine.text_standardizer import standardize_text
from cleaning_engine.special_char_handler import remove_special_characters
from cleaning_engine.constant_column_handler import remove_constant_columns
from cleaning_engine.high_missing_handler import remove_high_missing_columns
from cleaning_engine.space_cleaner import clean_spaces
from cleaning_engine.outlier_handler import remove_outliers
from cleaning_engine.json_name_extractor import extract_names
from cleaning_engine.stopword_handler import remove_stopwords


def apply_cleaning_pipeline(filtered_df, options):

    cleaned_df = filtered_df.copy()

    if options.get('remove_null_values'):
        for col in options.get('null_columns', []):
            cleaned_df = remove_nulls(cleaned_df, col)

    if options.get('remove_duplicate_rows'):
        cleaned_df = remove_duplicates(cleaned_df)

    if options.get('remove_empty_cols'):
        cleaned_df = remove_empty_columns(cleaned_df)

    if options.get('fix_data_types'):
        for col in options.get('datatype_columns', []):
            cleaned_df = fix_datatypes(cleaned_df, col)

    if options.get('fill_missing'):
        for col in options.get('fill_columns', []):
            cleaned_df = fill_missing_values(cleaned_df, col)

    if options.get('standardize_text_option'):
        for col in options.get('text_standard_columns', []):
            cleaned_df = standardize_text(cleaned_df, col)

    if options.get('remove_special_chars'):
        for col in options.get('special_char_columns', []):
            cleaned_df = remove_special_characters(cleaned_df, col)

    if options.get('remove_constant_cols'):
        cleaned_df = remove_constant_columns(cleaned_df)

    if options.get('remove_high_missing_cols'):
        cleaned_df = remove_high_missing_columns(cleaned_df)

    if options.get('remove_spaces'):
        for col in options.get('space_columns', []):
            cleaned_df = clean_spaces(cleaned_df, col)

    if options.get('remove_outlier_rows'):
        for col in options.get('outlier_columns', []):
            cleaned_df = remove_outliers(cleaned_df, col)

    if options.get('extract_json_names'):
        for col in options.get('json_columns', []):
            cleaned_df = extract_names(cleaned_df, col)

    if options.get('remove_stop_words'):
        for col in options.get('stopword_columns', []):
            cleaned_df = remove_stopwords(cleaned_df, col)

    return cleaned_df