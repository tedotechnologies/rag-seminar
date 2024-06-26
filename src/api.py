import uvicorn
import weaviate
from fastapi import FastAPI, Request, UploadFile, File
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from consts import TOP_K_DOCUMENTS, MODEL_URL, MAX_NEW_TOKENS, TEMPERATURE, DB_HOST, DB_PORT, WEA_APIKEY_KEY, \
    EMBEDDINGS_MODEL_NAME, API_PORT
from init_db import init_db
from llm_utils import call_model, get_messages
from script_utils import get_logger

app = FastAPI()

LOGGER = get_logger()


@app.post('/answer')
async def answer(
        request: Request,
):
    """
    Answer the question. Requires a JSON with a 'query' field.
    """
    data = await request.json()
    # get the query from the request
    query = """YOUR CODE HERE"""
    LOGGER.info(f"Got query: {query}")
    # get similar context from db
    context_fragments = """YOUR CODE HERE"""

    context = ''
    for fragment in context_fragments:
        # get the text content from the fragment
        fragment = """YOUR CODE HERE"""
        # add the fragment to the context
        context += """YOUR CODE HERE"""
    LOGGER.debug(f"Got context: {context}")

    # complete the code for the get_messages function in llm_utils.py
    # and add all the necessary arguments
    messages = get_messages()

    # add all the necessary arguments to the call_model function in llm_utils.py
    answer = await call_model()

    return {"answer": answer}


@app.post('/load_document')
async def load_document(
        request: Request,
        files: list[UploadFile] = File(...)
):
    ip_user = request.client.host
    LOGGER.info(f"Got request from {ip_user}")
    for file in files:
        with open(file.filename, "wb") as buffer:
            buffer.write(file.file.read())
        # initialize docx fileloader
        loader = """YOUR CODE HERE"""
        # load document
        document = """YOUR CODE HERE"""
        # initialize text splitter
        text_splitter = """YOUR CODE HERE"""
        # split text
        texts = """YOUR CODE HERE"""
        # add texts to db
        """YOUR CODE HERE"""
        LOGGER.info(f"Added document {file.filename} to DB")
    return {"answer": "Success!"}


if __name__ == "__main__":
    client = weaviate.Client(
        url=f"http://{DB_HOST}:{DB_PORT}",
        auth_client_secret=weaviate.AuthApiKey(WEA_APIKEY_KEY)
    )
    embeddings = OpenAIEmbeddings(
        model=EMBEDDINGS_MODEL_NAME
    )

    # complete the code for the init_db function in init_db.py
    # and add all the necessary arguments
    db = init_db()

    uvicorn.run(app, host="0.0.0.0", port=API_PORT, log_level="info")
