import streamlit as st
import requests

st.title("🚗 Smart Parking Management AI")

location = st.text_input("Enter your location")
if st.button("Find Parking"):
    data = {"location": location, "request_type": "find"}
    response = requests.post("https://abxxth.app.n8n.cloud/webhook/4f7610c3-0975-4fa3-bedc-b447758a8f6e", json=data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Available spots: {result['available_spots']}")
        st.info(f"Nearest spot: {result['nearest_spot']}")
        st.markdown(f"[Get Directions]({result['navigation_link']})")
    else:

        st.error("Error fetching parking info")



