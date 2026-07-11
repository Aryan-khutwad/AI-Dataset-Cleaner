import streamlit as st


def show_preview(df, title):

    st.subheader(title)

    st.dataframe(df.head())

    st.write("Dataset Shape")
    st.write(df.shape)