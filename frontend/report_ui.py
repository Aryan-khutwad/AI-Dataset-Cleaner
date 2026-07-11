import streamlit as st


def show_report(report):

    st.subheader("Cleaning Report")

    for key, value in report.items():
        st.write(f"{key}: {value}")