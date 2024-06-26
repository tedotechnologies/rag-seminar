import streamlit as st
import json
import requests

API_URL = "http://backend:5000"


def upload_files(files):
    files = [('files', file) for file in files]
    response = requests.post(f"{API_URL}/load_document", files=files)
    if response.status_code != 200:
        return False
    return response.json()


def main():
    st.title("Chatbot")
    user_input = st.text_area("Enter your question", height=200)
    if st.button("Send"):
        response = requests.post(f"{API_URL}/answer", json={"query": user_input})
        response = json.loads(response.text)["answer"]
        st.text_area("Response", value=response, height=200)
    else:
        st.warning("Please enter a question")
    uploaded_files = st.file_uploader("Select files to upload", accept_multiple_files=True)
    if uploaded_files is not None:
        if st.button("Upload"):
            response = upload_files(uploaded_files)
            if response:
                st.success("Files uploaded successfully")
            else:
                st.error("Failed to upload files")


if __name__ == "__main__":
    main()
