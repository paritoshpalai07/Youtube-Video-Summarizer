import streamlit as st


pages = {
    "About" : [
        st.Page("pages/home.py", title="📁 About Project"),
    ],
    "App" : [
        st.Page("pages/summarizer.py", title="🤖 Youtube Summarizer"),
    ]
}

pg = st.navigation(pages)

pg.run()
