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

from backend.decision_engine import (
    detect_column_type,
    should_fill_missing,
    should_remove_null_rows
)


def auto_clean_dataset(df):

    cleaned_df = df.copy()

    cleaning_log = []

    # ---------------- GLOBAL CLEANING ---------------- #

    cleaned_df = remove_duplicates(cleaned_df)
    cleaning_log.append({
        "Method": "Remove Duplicates",
        "Column": "All Dataset"
    })

    cleaned_df = remove_empty_columns(cleaned_df)
    cleaning_log.append({
        "Method": "Remove Empty Columns",
        "Column": "All Dataset"
    })

    cleaned_df = remove_constant_columns(cleaned_df)
    cleaning_log.append({
        "Method": "Remove Constant Columns",
        "Column": "All Dataset"
    })

    cleaned_df = remove_high_missing_columns(cleaned_df)
    cleaning_log.append({
        "Method": "Remove Highly Missing Columns",
        "Column": "All Dataset"
    })

    # ---------------- COLUMN CLEANING ---------------- #

    for column in cleaned_df.columns.tolist():

        try:

            column_type = detect_column_type(cleaned_df, column)

            # ---------- JSON ---------- #

            if column_type == "json":

                cleaned_df = extract_names(cleaned_df, column)

                cleaning_log.append({
                    "Method": "JSON Extraction",
                    "Column": column
                })

                continue

            # ---------- Datatype ---------- #

            cleaned_df = fix_datatypes(cleaned_df, column)

            cleaning_log.append({
                "Method": "Fix Datatype",
                "Column": column
            })

            # ---------- Missing ---------- #

            if should_fill_missing(cleaned_df, column):

                cleaned_df = fill_missing_values(cleaned_df, column)

                cleaning_log.append({
                    "Method": "Fill Missing",
                    "Column": column
                })

            elif should_remove_null_rows(cleaned_df, column):

                cleaned_df = remove_nulls(cleaned_df, column)

                cleaning_log.append({
                    "Method": "Remove Null Rows",
                    "Column": column
                })

            # ---------- Text ---------- #

            if column_type == "text":

                cleaned_df = standardize_text(cleaned_df, column)
                cleaned_df = remove_special_characters(cleaned_df, column)
                cleaned_df = clean_spaces(cleaned_df, column)
                cleaned_df = remove_stopwords(cleaned_df, column)

                cleaning_log.append({
                    "Method": "Text Cleaning",
                    "Column": column
                })

            # ---------- Numeric ---------- #

            if column_type == "numeric":

                cleaned_df = remove_outliers(cleaned_df, column)

                cleaning_log.append({
                    "Method": "Outlier Removal",
                    "Column": column
                })

        except Exception as e:

            cleaning_log.append({
                "Method": "Skipped",
                "Column": column,
                "Reason": str(e)
            })

    return cleaned_df, cleaning_log