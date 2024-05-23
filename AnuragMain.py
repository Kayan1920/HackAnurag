import streamlit as st
import webbrowser
import hashlib
import time
import base64
import streamlit as st
import requests
import pandas as pd

st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)

MAX_ATTEMPTS = 10

try:
    num_attempts = pd.read_csv("NumTries.csv")
except:
    num_attempts = pd.DataFrame([['Anurag', 0]], columns = ['Name', 'NumTries'])
    num_attempts.to_csv("NumTries.csv", index=False)

def set_gif_background(gif_url):
    gif_data = base64.b64encode(requests.get(gif_url).content)
    st.markdown(
    f"""
    <style>
    .stApp {{
        background: url(data:image/gif;base64,{gif_data.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

gif_url = 'https://i.gifer.com/3HeZ.gif' # replace with your gif url
set_gif_background(gif_url)

st.markdown('''<h1 style="color:white;">CTF Challenge</h1>''', unsafe_allow_html=True)

st.write("$$\\color{white}{\\text{Guess this four digit flag to reveal our intentions. - Courtesy of Kayan and Ayushi (tm)}}$$")
st.markdown("<p style='color:white'>Clue #1 : Thou hath already posses this key within thy mobile.</p>", unsafe_allow_html=True)
st.markdown("<p style='color:white'>Clue #2 : Despite numerous awards and accolades perhaps a recent and novel accomplishment holds the true secret.</p>", unsafe_allow_html=True)
st.markdown("<p style='color:white'>Clue #3 : Image</p>", unsafe_allow_html=True)
st.image("UnknownLogo.jpeg", caption="The image we were just talking about.")


with st.popover("Get a hint -> Lose 5 pts"):
    st.error("Really Anurag? A hint?")
    st.image("Judgement.jpeg",caption="Our face when you ask for hints.")

# Text input for flag
flag = st.text_input("Enter the flag:")


def check_flag():
    global flag, num_attempts

    num_attempts = pd.read_csv("NumTries.csv")
    if num_attempts.iloc[0, 1] >= MAX_ATTEMPTS:
        st.error("You have exceeded the maximum number of tries. Contact Kayan for further assistance.")
        return 
    
    

    hash = hashlib.md5(flag.encode())
    hash = hash.hexdigest()
    if hash == "6346dc723395e1ee8ef57f4883be4cb4":
        url = f"https://eservices.moec.gov.ae/eservices/Certificate?D=3085803&lang=en"
        st.error("Congrats! You're a nerd. You must accept reality before life moves on.")
        st.image("AnuragNerd.jpeg", caption="Anurag is a nerd")
        st.link_button("Click to reveal the memory associated with this CTF.", url)

    else:
        num_attempts.iloc[0, 1] += 1
        num_attempts.to_csv("NumTries.csv", index=False)
        x = st.error("Noob")
        st.image("AnuragFail.JPG", caption="Anurag is a noob")

# Check if flag is correct
if st.button("Submit"):
    check_flag()

