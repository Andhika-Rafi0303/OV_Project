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

st.markdown("""
    <style>
        .top-right-corner {
            position: fixed;
            top: 10px;
            right: 10px;
            font-family: 'Courier New', Courier, monospace;
            color: #00FF00;
            background-color: rgba(0, 0, 0, 0.5); /* Optional: adds a semi-transparent background */
            font-size: 10px;
            padding: 5px;
            border-radius: 5px;
        }
    </style>
    <div class="top-right-corner">
        Looking for a GitHub logo? Nice try, but we’re not falling for that again.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style="
        color: #00FF00; 
        font-family: 'Courier New', Courier, monospace; 
        text-align: center;
    ">WOW, LOOK WHO DECIDED TO PLAY DETECTIVE—GOOD LUCK NOOB</h1>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="
        text-align: justify;
        font-family: 'Courier New', Courier, monospace;
        color: #00FF00;
        padding: 20px;
    ">
        <p>Welcome to the most thrilling corner of the internet, where secrets are revealed and identities are barely a mystery. I am R4PBD, your self-proclaimed digital deity. This site isn't just ordinary—it's a gateway to the so-called 'data' I've supposedly hacked. Here, you can check passenger IDs from a database that’s as exclusive as your average public list.</p>
        <p>Excited to uncover the earth-shattering secrets behind each code? Enter your passenger ID and witness the grand reveal of information that's bound to be as groundbreaking as a fortune cookie. But beware, this is not for the faint-hearted; it's for those who find excitement in the mundane. Under my ever-watchful eye, absolutely nothing remains hidden.</p>
        <p>Step into my so-called world, where reality and digital fluff blur, and get ready for mind-blowing revelations that might change your perspective on, well, absolutely nothing. Welcome to the domain of R4PBD, where the ‘truth’ is just a click away—if you’re into that sort of thing.</p>
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
    # Create two columns for side-by-side layout
    col1, col2 = st.columns([1, 3], vertical_alignment = 'bottom')  # Adjust column widths as needed

    # Input field in the first column
    with col1:
        token_input = st.text_input("Input Passenger ID")

    # Submit button in the second column
    with col2:
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
                    st.session_state.message = "Seriously? Better luck next time, LOSER!!!"
            else:
                st.session_state.show_message = True
                st.session_state.message_type = 'error'
                st.session_state.message = "Input the ID, FOOL!!!"

# Display message
if st.session_state.show_message:
    st.markdown(display_message(st.session_state.message, st.session_state.message_type), unsafe_allow_html=True)
    # Reset the message after displaying it
    st.session_state.show_message = False

st.markdown("""
    <style>
        .bottom-left-corner {
            position: fixed;
            bottom: 10px;
            left: 10px;
            font-family: 'Courier New', Courier, monospace;
            color: #00FF00;
            font-size: 12px;
            background-color: rgba(0, 0, 0, 0.5); /* Optional: adds a semi-transparent background */
            padding: 5px;
            border-radius: 5px;
        }
    </style>
    <div class="bottom-left-corner">
        &copy; 2024 R4PBD. All rights reserved. (Like anyone would actually try to copy this gem.)<br>
    </div>
""", unsafe_allow_html=True)

