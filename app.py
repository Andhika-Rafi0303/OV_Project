import streamlit as st
import time

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
footer > div:first-of-type {visibility: hidden;} /* Menyembunyikan "Hosted with Streamlit" */
</style>
"""

# Menyematkan CSS dalam aplikasi Streamlit
st.markdown(hide_st_style, unsafe_allow_html=True)

def display_message(message, status):
    if status == 'success':
        st.markdown(f"<div style='background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px; text-align: center;'><strong>{message}</strong></div>", unsafe_allow_html=True)
    elif status == 'error':
        st.markdown(f"<div style='background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; text-align: center;'><strong>{message}</strong></div>", unsafe_allow_html=True)

# Load tokens from secrets
tokens_dict = st.secrets["tokens"]

if 'url_displayed' not in st.session_state:
    st.session_state.url_displayed = False
if 'url' not in st.session_state:
    st.session_state.url = ""

col1, col2 = st.columns([1, 1], vertical_alignment='center')
with col1:
    st.image('Logo_MBC.png', use_column_width=True)
with col2:
    st.image('Logo_BD.png', use_column_width=True)

st.title("Token Verification System")

token_input = st.text_input("Masukkan Token")

if st.button("Submit"):
    if token_input:
        url = tokens_dict.get(token_input)
        if url:
            st.session_state.url = url
            st.session_state.url_displayed = True
            st.success("Token valid. Here is your URL:")
            st.session_state.show_url = True
            # Timer to hide URL after 5 seconds
            time.sleep(5)
            st.session_state.url_displayed = False
            st.session_state.url = ""
        else:
            display_message("Jawaban salah", 'error')
    else:
        st.warning("Token harus diisi.")

if st.session_state.url_displayed:
    st.markdown(f"<a href='{st.session_state.url}' target='_blank'>{st.session_state.url}</a>", unsafe_allow_html=True)
