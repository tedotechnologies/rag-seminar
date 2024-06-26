import weaviate
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain_community.vectorstores import Weaviate
from langchain_text_splitters import RecursiveCharacterTextSplitter

from consts import PATH_TO_DOCUMENTS
from script_utils import get_logger

LOGGER = get_logger(__name__)


def init_db(
        client: weaviate.Client,
        embeddings: OpenAIEmbeddings | HuggingFaceEmbeddings
)-> Weaviate:
    """
    Initialize Weaviate DB with documents from PATH_TO_DOCUMENTS.

    Parameters:
    client: weaviate.Client
        Weaviate client.
    embeddings: OpenAIEmbeddings | HuggingFaceEmbeddings
        Embeddings model.

    Returns:
    db :Weaviate
        Weaviate DB.
    """
    # initialize loader with PATH_TO_DOCUMENTS
    loader = """YOUR CODE HERE"""
    # load documents
    documents = """YOUR CODE HERE"""
    # initialize text splitter
    text_splitter = """YOUR CODE HERE"""
    # split documents
    docs = """YOUR CODE HERE"""
    LOGGER.info("Loading DB from files...")

    # initialize Weaviate DB from documents
    db = Weaviate.from_documents(
        documents=docs,
        embedding=embeddings,
        client=client
    )
    return db
