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
):
    loader = Docx2txtLoader(str(PATH_TO_DOCUMENTS))
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0
    )
    docs = text_splitter.split_documents(documents)
    LOGGER.info("Loading DB from files...")
    db = Weaviate.from_documents(
        documents=docs,
        embedding=embeddings,
        client=client
    )
    return db
