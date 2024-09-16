import streamlit as st
import random

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
footer > div:first-of-type {visibility: hidden;} /* Hide "Hosted with Streamlit" */
body {display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; flex-direction: column;}
input[type='text'] {width: 300px; padding: 10px; font-size: 18px;} /* Adjust input field width and padding */
.stAlert {font-size: 20px;} /* Increase font size of notifications */
a {color: blue; text-decoration: underline;} /* Style links */
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
if 'message_type' not in st.session_state:
    st.session_state.message_type = ''
if 'message' not in st.session_state:
    st.session_state.message = ''
if 'url' not in st.session_state:
    st.session_state.url = ''

st.title("THE ANSWER IS NEAR")

st.markdown("""
<style>
    body {
        font-family: 'Courier New', Courier, monospace; /* Terminal-like font */
        color: #00FF00; /* Terminal green text color */
        background-color: #000000; /* Terminal black background color */
    }

    .justify {
        text-align: justify;
    }

    /* Optional: Style for links to match terminal theme */
    a {
        color: #00FF00; /* Terminal green link color */
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
</style>

<div class="justify">
    Welcome to the dark side of the world, where secrets are unveiled and identities laid bare. I am R4PBD, the enigmatic overlord of the digital shadows. This is not just any ordinary site—it's a portal into the depths of the data I've meticulously hacked. Here, you have the power to check passenger IDs from an exclusive, clandestine database.
    <br><br>
    Are you ready to uncover the hidden stories behind each code? Enter your passenger ID and let the veil of mystery be lifted. Every digit, every character holds a secret waiting to be discovered. But beware, this realm is not for the faint-hearted. Here, under the watchful eyes of R4PBD, nothing can be concealed.
    <br><br>
    Step into my world, where the lines between reality and the digital void blur, and prepare yourself for revelations that could change everything you thought you knew. Welcome to the domain of R4PBD, where the truth is just a click away.
</div>
""", unsafe_allow_html=True)


phrases = [
    "Wow, you actually got it right? <a href='{url}' target='_blank'>NEXT CLUE</a>—don’t get used to it; luck won’t always save you.",
    "Well, look at you, getting it right! <a href='{url}' target='_blank'>CLICK HERE FOR THE NEXT CLUE</a>—don’t let this success go to your head.",
    "Congratulations! considering it was probably just a lucky guess. <a href='{url}' target='_blank'>HERE’S YOUR NEXT CLUE</a>.",
    "Well, aren’t you a genius? <a href='{url}' target='_blank'>FIND YOUR NEXT CLUE HERE</a>—not that it’ll be any easier."
]

# Centered input and button
with st.container():
    st.write("<div style='text-align: center;'>", unsafe_allow_html=True)
    token_input = st.text_input("Input Pasengges ID")
    if st.button("Submit"):
        if token_input:
            url = tokens_dict.get(token_input)
            if url:
                st.session_state.url = url
                st.session_state.show_message = True
                st.session_state.message_type = 'success'
                st.session_state.message = random.choice(phrases).format(url=url)
            else:
                st.session_state.show_message = True
                st.session_state.message_type = 'error'
                st.session_state.message = "Seriously? Wrong again. Better luck next time, LOSER."
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
