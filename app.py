import streamlit as st
import pandas as pd

# Frontend
from frontend.upload_ui import upload_dataset
from frontend.preview_ui import show_preview
from frontend.profile_ui import show_profile
from frontend.cleaning_ui import get_cleaning_options
from frontend.report_ui import show_report

# Backend
from backend.file_handler import load_dataset
from backend.cleaning_pipeline import apply_cleaning_pipeline
from backend.auto_cleaner import auto_clean_dataset

# Utils
from utils.data_profiler import profile_data, column_profile
from utils.report_generator import generate_report
from utils.auto_clean_report import generate_auto_clean_report


# ---------------- App Title ---------------- #

st.title("AI Dataset Cleaner")


# ---------------- Upload Dataset ---------------- #

uploaded_file = upload_dataset()


# ---------------- Main Workflow ---------------- #

if uploaded_file is not None:

    # Load Dataset
    df = load_dataset(uploaded_file)

    st.success("Dataset Uploaded Successfully")

    # ---------------- Original Dataset ---------------- #

    show_preview(df, "Original Dataset")

    # ---------------- Dataset Profile ---------------- #

    profile = profile_data(df)
    column_info = column_profile(df)

    show_profile(profile, column_info)

    # ---------------- Feature Selection ---------------- #

    st.subheader("Select Columns to Keep")

    selected_columns = st.multiselect(
        "Choose Features",
        df.columns.tolist(),
        default=df.columns.tolist()
    )

    filtered_df = df[selected_columns]

    # ---------------- Filtered Dataset ---------------- #

    show_preview(filtered_df, "Filtered Dataset")

    # ---------------- Cleaning Mode ---------------- #

    st.subheader("Cleaning Mode")

    auto_clean = st.button("Auto Clean Dataset")

    cleaning_log = None


    # ---------------- Cleaning Pipeline ---------------- #

    if auto_clean:

        cleaned_df, cleaning_log = auto_clean_dataset(filtered_df)

    else:

        options = get_cleaning_options(filtered_df)

        cleaned_df = apply_cleaning_pipeline(
            filtered_df,
            options
        )
    # ---------------- Cleaned Dataset ---------------- #

    show_preview(cleaned_df, "Cleaned Dataset")

    # ---------------- Auto Cleaning Report ---------------- #

    if cleaning_log is not None:

        st.subheader("Auto Cleaning Report")

        report_df = generate_auto_clean_report(cleaning_log)

        st.dataframe(report_df)

    # ---------------- Report ---------------- #

    report = generate_report(filtered_df, cleaned_df)

    show_report(report)

    # ---------------- Download ---------------- #

    st.subheader("Download Cleaned Dataset")

    csv = cleaned_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Cleaned CSV",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )

    # ---------------- Column Names ---------------- #

    st.subheader("Column Names")
    st.write(df.columns.tolist())