import streamlit as st
import webbrowser
import hashlib
import time

# Page title
st.title("CTF Challenge")

# Text input for flag
flag = st.text_input("Enter the flag:")

# Check if flag is correct
if st.button("Submit"):
    hash = hashlib.md5(flag.encode())
    hash = hash.hexdigest()
    if hash == "6346dc723395e1ee8ef57f4883be4cb4":
        url = f"https://eservices.moec.gov.ae/eservices/Certificate?D=3085803&lang=en"
        st.error("Congrats! You're a nerd. You have ten seconds to accept reality before life moves on.")
        st.image("AnuragNerd.JPEG", caption="Anurag is a nerd")
        time.sleep(10)
        webbrowser.open(url, new=1)
    else:
        x = st.error("Noob")
        st.image("AnuragFail.JPG", caption="Anurag is a noob")
