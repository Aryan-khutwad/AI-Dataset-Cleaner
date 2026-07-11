import streamlit as st


def upload_dataset():

    uploaded_file = st.file_uploader(
        "Upload Dataset",
        type=["csv", "xlsx", "json"]
    )

    return uploaded_file