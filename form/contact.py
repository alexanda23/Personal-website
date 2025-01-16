import streamlit as st
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]


def is_valid_email(email:str) -> bool:
    #localpart@domain
    specialchar = "-+=!#$%$^&*()~`:;,><?|"
    if "@" in email and "." in email and not any(char in specialchar for char in email):
        if email.index("@") != 0 and email.index("@") != (len(email) - 1):
            splitted = email.split("@")[-1]
            domain = splitted.split(".")[-1]
            if len(domain) >= 2 and ".." not in splitted:
                return True
                
    return False
                



@st.dialog("Contact Me")



def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First name")
        email = st.text_input("Email Address")
        message = st.text_area("Your message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not name:
                st.error("Email service is not set up. Please try again later.", icon="❌")
                st.stop

            if not email:
                st.error("Please provide your name.", icon="❌")
                st.stop
            
            if not is_valid_email:
                st.error("Email is not valid, please provide a valid Email", icon = "❌")
                st.stop

            if not message:
                st.error("Please provide a message.", icon="❌")
                st.stop

            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message has been sent successfully! 🎉", icon="🚀")
            else:
                st.error("There was an error sending your message.", icon="😨")



