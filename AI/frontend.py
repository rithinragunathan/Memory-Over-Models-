import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="Hackathon Assistant", layout="wide")

st.title("🧠 Hackathon Resource Assistant")
st.markdown("Ask about rules, themes, or deadlines. Powered by **Qdrant**.")

query = st.text_input("Ask a question:")

if st.button("Search Memory"):
    if query:
        with st.spinner("Retrieving from Qdrant..."):
            try:
                res = requests.post(BACKEND_URL, json={"question": query})
                if res.status_code == 200:
                    data = res.json()
                    
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.subheader("Answer")
                        st.write(data["answer"])
                    
                    with col2:
                        st.subheader("Source Context")
                        for idx, source in enumerate(data["context"]):
                            st.info(f"{idx+1}. {source}")
                else:
                    st.error("Backend Error")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")