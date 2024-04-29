import streamlit as st

def main():
    menu = ["UK", "US"]
    choice = st.sidebar.selectbox("Select Country", menu)

    if choice == "UK":
        st.subheader("United Kingdom")
        raw_data = st.text_area("Input your data here")

    elif choice == "US":
        st.subheader("United States")
        raw_data = st.text_area("Input your data here")

    if st.button("Send request"):
        st.info("Your request has been sent. Thank you for your patience.")