import streamlit as st


def get_cleaning_options(filtered_df):

    options = {}

    all_columns = filtered_df.columns.tolist()

    text_columns = filtered_df.select_dtypes(
        include='object'
    ).columns.tolist()

    numeric_columns = filtered_df.select_dtypes(
        include=['int64', 'float64']
    ).columns.tolist()

    st.subheader("Cleaning Options")

    

    options['remove_null_values'] = st.checkbox("Remove Null Values")

    if options['remove_null_values']:
        options['null_columns'] = st.multiselect(
            "Select Columns for Null Removal",
            all_columns
        )

    options['remove_duplicate_rows'] = st.checkbox("Remove Duplicate Rows")

    options['remove_empty_cols'] = st.checkbox("Remove Empty Columns")

    options['fix_data_types'] = st.checkbox("Fix Datatypes")

    if options['fix_data_types']:
        options['datatype_columns'] = st.multiselect(
            "Select Columns for Datatype Fix",
            all_columns
        )

    options['fill_missing'] = st.checkbox("Fill Missing Values")

    if options['fill_missing']:
        options['fill_columns'] = st.multiselect(
            "Select Columns for Fill Missing",
            all_columns
        )
    
    options['standardize_text_option'] = st.checkbox("Standardize Text")

    if options['standardize_text_option']:
        options['text_standard_columns'] = st.multiselect(
            "Select Columns for Text Standardization",
            text_columns
        )

    options['remove_special_chars'] = st.checkbox("Remove Special Characters")

    if options['remove_special_chars']:
        options['special_char_columns'] = st.multiselect(
            "Select Columns for Special Character Removal",
            text_columns
        )

    options['remove_constant_cols'] = st.checkbox("Remove Constant Columns")

    options['remove_high_missing_cols'] = st.checkbox("Remove Highly Missing Columns")

    options['remove_spaces'] = st.checkbox("Remove Extra Spaces")

    if options['remove_spaces']:
        options['space_columns'] = st.multiselect(
            "Select Columns for Space Cleaning",
            text_columns
        )

    options['remove_outlier_rows'] = st.checkbox("Remove Outliers")

    if options['remove_outlier_rows']:
        options['outlier_columns'] = st.multiselect(
            "Select Columns for Outlier Removal",
            numeric_columns
        )

    options['extract_json_names'] = st.checkbox("Extract Names From JSON Column")

    if options['extract_json_names']:
        options['json_columns'] = st.multiselect(
            "Select JSON Columns",
            all_columns
        )

    options['remove_stop_words'] = st.checkbox("Remove Stop Words")

    if options['remove_stop_words']:
        options['stopword_columns'] = st.multiselect(
            "Select Columns for Stop Word Removal",
            text_columns
        )

    return options