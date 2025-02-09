import streamlit as st 
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="Streamlit yohan ynov",
    page_icon="😎",
    layout="wide",
)

st.sidebar.title("Affichage d'une page web dans Streamlit")


st.markdown(
f'<iframe src="{"https://fastapi-yohan-ynov-b4e8901d7995.herokuapp.com/docs"}" width="100%" height="1000px" style="border:none; overflow:auto;"></iframe>',
unsafe_allow_html=True
)