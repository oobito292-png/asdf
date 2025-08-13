import streamlit as st
import requests

st.title("🚗 Smart Parking Management AI")

location = st.text_input("Enter your location")
if st.button("Find Parking"):
    data = {"location": location, "request_type": "find"}
    response = requests.post("https://abxxth.app.n8n.cloud/webhook-test/parkinginfo", json=data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Available spots: {result['available_spots']}")
        st.info(f"Nearest spot: {result['nearest_spot']}")
        st.markdown(f"[Get Directions]({result['navigation_link']})")
    else:

        st.error("Error fetching parking info")

