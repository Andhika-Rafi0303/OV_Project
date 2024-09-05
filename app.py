import streamlit as st

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
footer > div:first-of-type {visibility: hidden;} /* Hide "Hosted with Streamlit" */
body {display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; flex-direction: column;}
input[type='text'] {width: 300px; padding: 10px; font-size: 18px;} /* Adjust input field width and padding */
.stAlert {font-size: 20px;} /* Increase font size of notifications */
</style>
"""

# Embed CSS in the Streamlit app
st.markdown(hide_st_style, unsafe_allow_html=True)

def display_message(message, status):
    if status == 'success':
        return f"<div class='stAlert' style='background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px; text-align: center;'><strong>{message}</strong></div>"
    elif status == 'error':
        return f"<div class='stAlert' style='background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; text-align: center;'><strong>{message}</strong></div>"
    elif status == 'warning':
        return f"<div class='stAlert' style='background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; text-align: center;'><strong>{message}</strong></div>"
    return ""

# Load tokens from secrets
tokens_dict = st.secrets["tokens"]

# Initialize session state variables
if 'show_message' not in st.session_state:
    st.session_state.show_message = False
if 'url' not in st.session_state:
    st.session_state.url = ""
if 'message_type' not in st.session_state:
    st.session_state.message_type = ''
if 'message' not in st.session_state:
    st.session_state.message = ''

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
                st.session_state.message_type = 'success'
                st.session_state.message = f"Token valid. Here is your URL: {url}"
            else:
                st.session_state.show_message = True
                st.session_state.message_type = 'error'
                st.session_state.message = "Jawaban salah"
        else:
            st.session_state.show_message = True
            st.session_state.message_type = 'error'
            st.session_state.message = "Token harus diisi."
    st.write("</div>", unsafe_allow_html=True)

# Display message
if st.session_state.show_message:
    st.markdown(display_message(st.session_state.message, st.session_state.message_type), unsafe_allow_html=True)
    # Reset the message after displaying it
    st.session_state.show_message = False
