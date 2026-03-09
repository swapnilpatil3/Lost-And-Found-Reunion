import streamlit as st

st.title("Lost & Found Reunion 🔍")

st.write("Search for your lost item")

query = st.text_input("Enter item description")

if st.button("Search"):
    
    if query:
        st.write("Result 1: Apple AirPods Max found near library")
        st.write("Result 2: Sony Headphones found near classroom")
        st.write("Result 3: Boat Wireless Earbuds found near canteen")

        st.write("AI Explanation: These items match your description of headphones.")
