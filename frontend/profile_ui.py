import streamlit as st
import pandas as pd


def show_profile(profile, column_info):

    st.subheader("Dataset Profile")

    for key, value in profile.items():
        st.write(f"{key}: {value}")

    st.subheader("Column Insights")

    column_df = pd.DataFrame(column_info)
    st.dataframe(column_df)