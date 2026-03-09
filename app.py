import streamlit as st
from scripts.search_engine import search_items

st.title("🔍 Lost & Found Reunion")

st.write("Search lost items using natural language")

query = st.text_input("Enter item description")

if st.button("Search"):

    results = search_items(query)

    st.subheader("Matching Items")

    for i,item in enumerate(results["documents"][0]):

        st.write(f"### Result {i+1}")
        st.write(item)

        explanation = f"This result matches your query because the semantic meaning of the description is similar."

        st.write("AI Explanation:", explanation)
