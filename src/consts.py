import os
from pathlib import Path

ROOT_PATH = Path(__file__).parents[1]
PATH_TO_DOCUMENTS = ROOT_PATH / "documents/rules_fiim.docx"

DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
WEA_APIKEY_KEY = os.environ["AUTHENTIFICATION_APIKEY_ALLOWED_KEYS"]
TOP_K_DOCUMENTS = int(os.environ["TOP_K_DOCUMENTS"])

SYSTEM_PROMPT = os.environ["SYSTEM_PROMPT"]

MODEL_URL = os.environ["MODEL_URL"]
MODEL_NAME = os.environ["MODEL_NAME"]
EMBEDDINGS_MODEL_NAME = os.environ["EMBEDDINGS_MODEL_NAME"]

OPENAI_TOKEN = os.environ["OPENAI_API_KEY"]
MAX_NEW_TOKENS = int(os.environ["MAX_NEW_TOKENS"])
TEMPERATURE = float(os.environ["TEMPERATURE"])

API_PORT = int(os.environ["API_PORT"])
