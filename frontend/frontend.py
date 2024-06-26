import streamlit as st
import json
import requests

# Use the name of the backend container and an internal port if running in Docker
API_URL = "http://<>:<>"


def upload_files(files):
    files = [('files', file) for file in files]
    # send the files in a POST request to the backend to load them
    response = """YOUR CODE HERE"""
    if response.status_code != 200:
        return False
    return response.json()


def main():
    st.title("Chatbot")
    user_input = st.text_area("Enter your question", height=200)
    if st.button("Send"):
        # send the question in a POST request to the backend to get the answer
        response = """YOUR CODE HERE"""
        # get the answer from the response
        response = """YOUR CODE HERE"""
        st.text_area("Response", value=response, height=200)
    else:
        st.warning("Please enter a question")
    uploaded_files = st.file_uploader("Select files to upload", accept_multiple_files=True)
    if uploaded_files is not None:
        if st.button("Upload"):
            # complete the upload_files function above
            response = upload_files(uploaded_files)
            if response:
                st.success("Files uploaded successfully")
            else:
                st.error("Failed to upload files")


if __name__ == "__main__":
    main()
