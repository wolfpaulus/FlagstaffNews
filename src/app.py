""" Main application file for the Streamlit app """

import streamlit as st
from fetch_data import fetch_news


def main():
    st.title("Arizona Daily Sun News")
    news = fetch_news()
    for item in news:
        st.write(f"Title: {item['title']}")
        st.write(f"Link: {item['link']}")
        st.write(f"Description: {item['description']}")
        st.write("\n")


main()
