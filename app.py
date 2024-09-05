import streamlit as st

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
footer > div:first-of-type {visibility: hidden;} /* Menyembunyikan "Hosted with Streamlit" */
body {display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; flex-direction: column;}
input[type='text'] {width: 300px; padding: 10px; font-size: 18px;} /* Adjust input field width and padding */
.stAlert {font-size: 20px;} /* Increase font size of notifications */
</style>
"""

# Menyematkan CSS dalam aplikasi Streamlit
st.markdown(hide_st_style, unsafe_allow_html=True)

def display_message(message, status):
    if status == 'success':
        st.markdown(f"<div class='stAlert' style='background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px; text-align: center;'><strong>{message}</strong></div>", unsafe_allow_html=True)
    elif status == 'error':
        st.markdown(f"<div class='stAlert' style='background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; text-align: center;'><strong>{message}</strong></div>", unsafe_allow_html=True)
    elif status == 'warning':
        st.markdown(f"<div class='stAlert' style='background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; text-align: center;'><strong>{message}</strong></div>", unsafe_allow_html=True)

# Load tokens from secrets
tokens_dict = st.secrets["tokens"]

if 'show_message' not in st.session_state:
    st.session_state.show_message = False
if 'url' not in st.session_state:
    st.session_state.url = ""
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

col1, col2 = st.columns([1, 1], vertical_alignment='center')
with col1:
    st.image('Logo_MBC.png', use_column_width=True)
with col2:
    st.image('Logo_BD.png', use_column_width=True)

st.title("Token Verification System")

# Centered input and button
with st.container():
    st.write("<div style='text-align: center;'>", unsafe_allow_html=True)
    token_input = st.text_input("Masukkan Token")
    if st.button("Submit"):
        if token_input:
            url = tokens_dict.get(token_input)
            if url:
                st.session_state.url = url
                st.session_state.show_message = True
                st.session_state.start_time = st.experimental_get_query_params().get("start_time", [None])[0] or st.time()
                st.success(f"Token valid. Here is your URL: {url}")
            else:
                display_message("Jawaban salah", 'error')
        else:
            st.warning("Token harus diisi.")
    st.write("</div>", unsafe_allow_html=True)

# Check if URL should be displayed or if time has expired
if st.session_state.show_message:
    if st.session_state.start_time:
        elapsed_time = st.time() - st.session_state.start_time
        if elapsed_time >= 5:  # If 5 seconds have passed
            st.session_state.show_message = False
            st.session_state.url = ""
            display_message("Waktu habis", 'warning')
        else:
            # Still showing the URL for less than 5 seconds
            st.markdown(f"<div class='stAlert' style='background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px; text-align: center;'><strong>Token valid. Here is your URL: {st.session_state.url}</strong></div>", unsafe_allow_html=True)
