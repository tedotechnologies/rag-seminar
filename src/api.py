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
    data = await request.json()
    query = data.get('query')
    context_fragments = db.similarity_search(
        query=query,
        k=TOP_K_DOCUMENTS
    )
    context = ''
    for fragment in context_fragments:
        fragment = fragment.page_content
        context += f"{fragment}\n\n"
    LOGGER.debug(f"Got context: {context}")
    messages = get_messages(
        question=query,
        context=context
    )
    answer = await call_model(
        messages=messages,
        url_out=MODEL_URL,
        max_new_tokens=MAX_NEW_TOKENS,
        temperature=TEMPERATURE
    )
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
        loader = Docx2txtLoader(str(file.filename))
        document = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=0
        )
        texts = text_splitter.spit_text(document[0].page_content)
        db.add_texts(texts=texts)
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
    db = init_db(
        client,
        embeddings
    )
    uvicorn.run(app, host="0.0.0.0", port=API_PORT, log_level="info")
