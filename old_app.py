# import streamlit as st
# import pandas as pd
# from cleaning_engine.null_handler import remove_nulls
# from cleaning_engine.duplicate_handler import remove_duplicates
# from cleaning_engine.empty_column_handler import remove_empty_columns
# from cleaning_engine.datatype_handler import fix_datatypes
# from cleaning_engine.fill_missing_handler import fill_missing_values
# from cleaning_engine.text_standardizer import standardize_text
# from cleaning_engine.special_char_handler import remove_special_characters
# from cleaning_engine.constant_column_handler import remove_constant_columns
# from cleaning_engine.high_missing_handler import remove_high_missing_columns
# from cleaning_engine.space_cleaner import clean_spaces
# from cleaning_engine.outlier_handler import remove_outliers
# from cleaning_engine.json_name_extractor import extract_names
# from cleaning_engine.stopword_handler import remove_stopwords
# from utils.report_generator import generate_report
# from utils.data_profiler import profile_data
# from utils.data_profiler import column_profile


# st.title("AI Dataset Cleaner")

# uploaded_file = st.file_uploader(
#     "Upload Dataset",
#     type=["csv", "xlsx", "json"]
# )

# if uploaded_file is not None:

#     if uploaded_file.name.endswith(".csv"):
#         df = pd.read_csv(uploaded_file)

#     elif uploaded_file.name.endswith(".xlsx"):
#         df = pd.read_excel(uploaded_file)

#     elif uploaded_file.name.endswith(".json"):
#         df = pd.read_json(uploaded_file)

#     st.success("Dataset Uploaded Successfully")

#     profile = profile_data(df)
#     column_info = column_profile(df)

#     st.write("Dataset Preview")
#     st.dataframe(df.head())

#     # Original Dataset Preview

#     st.write("Original Dataset Shape")
#     st.write(df.shape)

    

#     st.subheader("Dataset Profile")

#     for key, value in profile.items():
#         st.write(f"{key}: {value}")

#     st.subheader("Column Insights")

#     column_df = pd.DataFrame(column_info)
#     st.dataframe(column_df)

#     st.write("Select Columns to Keep")

#     selected_columns = st.multiselect(
#         "Choose Features",
#         df.columns.tolist(),
#         default=df.columns.tolist()
#     )

#     filtered_df = df[selected_columns]

#     st.write("Filtered Dataset Preview")
#     st.dataframe(filtered_df.head())

#     # Filtered Dataset Preview

#     st.write("Filtered Dataset Shape")
#     st.write(filtered_df.shape)

#     # Cleaning Section
#     st.subheader("Cleaning Options")

#     # Column Lists
#     all_columns = filtered_df.columns.tolist()

#     text_columns = filtered_df.select_dtypes(
#         include='object'
#     ).columns.tolist()

#     numeric_columns = filtered_df.select_dtypes(
#         include=['int64', 'float64']
#     ).columns.tolist()


#     # ---------------- Cleaning Options ---------------- #

#     remove_null_values = st.checkbox("Remove Null Values")

#     if remove_null_values:
#         null_columns = st.multiselect(
#             "Select Columns for Null Removal",
#             all_columns
#         )


#     remove_duplicate_rows = st.checkbox("Remove Duplicate Rows")


#     remove_empty_cols = st.checkbox("Remove Empty Columns")


#     fix_data_types = st.checkbox("Fix Datatypes")

#     if fix_data_types:
#         datatype_columns = st.multiselect(
#             "Select Columns for Datatype Fix",
#             all_columns
#         )


#     fill_missing = st.checkbox("Fill Missing Values")

#     if fill_missing:
#         fill_columns = st.multiselect(
#             "Select Columns for Fill Missing",
#             all_columns
#         )


#     standardize_text_option = st.checkbox("Standardize Text")

#     if standardize_text_option:
#         text_standard_columns = st.multiselect(
#             "Select Columns for Text Standardization",
#             text_columns
#         )


#     remove_special_chars = st.checkbox("Remove Special Characters")

#     if remove_special_chars:
#         special_char_columns = st.multiselect(
#             "Select Columns for Special Character Removal",
#             text_columns
#         )


#     remove_constant_cols = st.checkbox("Remove Constant Columns")


#     remove_high_missing_cols = st.checkbox("Remove Highly Missing Columns")


#     remove_spaces = st.checkbox("Remove Extra Spaces")

#     if remove_spaces:
#         space_columns = st.multiselect(
#             "Select Columns for Space Cleaning",
#             text_columns
#         )


#     remove_outlier_rows = st.checkbox("Remove Outliers")

#     if remove_outlier_rows:
#         outlier_columns = st.multiselect(
#             "Select Columns for Outlier Removal",
#             numeric_columns
#         )
    
#     extract_json_names = st.checkbox("Extract Names From JSON Column")
    
#     if extract_json_names:
#         json_column = st.multiselect(
#             "Select JSON Columns",
#             all_columns
#         )
    
#     remove_stop_words = st.checkbox("Remove Stop Words")

#     if remove_stop_words:
#         stopword_columns = st.multiselect(
#             "Select Columns for Stop Word Removal",
#             text_columns
#         )

#     # Cleaning Logic
#     cleaned_df = filtered_df.copy()

#     # ---------------- Cleaning Pipeline ---------------- #

#     if remove_null_values:
#         for col in null_columns:
#             cleaned_df = remove_nulls(cleaned_df, col)

#     if remove_duplicate_rows:
#         cleaned_df = remove_duplicates(cleaned_df)

#     if remove_empty_cols:
#         cleaned_df = remove_empty_columns(cleaned_df)

#     if fix_data_types:
#         for col in datatype_columns:
#             cleaned_df = fix_datatypes(cleaned_df, col)

#     if fill_missing:
#         for col in fill_columns:
#             cleaned_df = fill_missing_values(cleaned_df, col)

#     if standardize_text_option:
#         for col in text_standard_columns:
#             cleaned_df = standardize_text(cleaned_df, col)

#     if remove_special_chars:
#         for col in special_char_columns:
#             cleaned_df = remove_special_characters(cleaned_df, col)

#     if remove_constant_cols:
#         cleaned_df = remove_constant_columns(cleaned_df)

#     if remove_high_missing_cols:
#         cleaned_df = remove_high_missing_columns(cleaned_df)

#     if remove_spaces:
#         for col in space_columns:
#             cleaned_df = clean_spaces(cleaned_df, col)

#     if remove_outlier_rows:
#         for col in outlier_columns:
#             cleaned_df = remove_outliers(cleaned_df, col)
    
#     if extract_json_names:
#         for col in json_column:
#             cleaned_df = extract_names(cleaned_df, col)

#     if remove_stop_words:
#         for col in stopword_columns:
#             cleaned_df = remove_stopwords(cleaned_df, col)
    
    
#     # Show Output
#     st.write("Cleaned Dataset")
#     st.dataframe(cleaned_df.head())

#     st.write("Cleaned Dataset Shape")
#     st.write(cleaned_df.shape)
    
#     # Generate Report
#     report = generate_report(filtered_df, cleaned_df)

#     st.subheader("Cleaning Report")

#     for key, value in report.items():
#         st.write(f"{key}: {value}")

#     st.subheader("Download Cleaned Dataset")

#     csv = cleaned_df.to_csv(index=False).encode('utf-8')

#     st.download_button(
#         label="Download Cleaned CSV",
#         data=csv,
#         file_name="cleaned_dataset.csv",
#         mime="text/csv"
#     )

#     st.write("Column Names")
#     st.write(df.columns.tolist())
