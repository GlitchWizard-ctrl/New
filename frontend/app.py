import streamlit as st
import requests

st.title("Greeting App")

name = st.text_input("Enter your name:")

if st.button("Greet Me"):
    if not name:
        st.error("Please enter your name.")
    else:
        try:
            response = requests.post(
                "https://new-kpn8.onrender.com/greet",  # your backend URL here
                json={"name": name}
            )
            response.raise_for_status()
            data = response.json()
            st.success(data.get("message", "No response from server"))

        except requests.exceptions.RequestException as e:
            st.error(f"Error contacting backend: {e}")
