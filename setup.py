from openinference.instrumentation.openai_agents import OpenAIAgentsInstrumentor
from agents.extensions.memory import MongoDBSession
from logger import logger, logging
from langfuse import get_client
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pinecone import Pinecone, QueryResponse
from constants import *
import nest_asyncio
import redis
import os

from utility import retry_thing

load_dotenv()

BASE_URL = os.getenv("BASE_URL") or ''
API_KEY = os.getenv("API_KEY") or ''
VDB_KEY = os.getenv("VDB_KEY") or ""
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY") or ""
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY") or ""
LANGFUSE_BASE_URL = os.getenv("LANGFUSE_BASE_URL") or ""
REDIS_URL = os.getenv("REDIS_URL") or ""
MONGO_URL = os.getenv("MONGO_URL") or ""
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME") or ""

# --- Model

if not BASE_URL or not API_KEY or not MODEL_NAME:
    logger.log(level=logging.ERROR, msg="BASE_URL, API_KEY, MODEL_NAME must be set via env var or code.")
    raise ValueError(
        "Please set BASE_URL, API_KEY, MODEL_NAME via env var or code."
    )
    
client = retry_thing(lambda:AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY))()

# --- Long Term Memory ( MongoDB )

logger.log(level=logging.INFO, msg="trying to connect Mongodb for long term memory")
try: 
    session = retry_thing(lambda : MongoDBSession.from_uri(
        USER_ID,
        uri=MONGO_URL,
        database=MONGO_DB_NAME,
    ))()
    logger.log(level=logging.INFO, msg="connected to Mongodb for long term memory")
except Exception as e:
    logger.log(level=logging.ERROR, msg=f"failed to connect to Mongodb for long term memory, error: {e}")


# --- Short Term State ( Redis )
logger.log(level=logging.INFO, msg="trying to connect redis for short term state")
try:
    redis_client = redis.Redis(
        host=REDIS_URL.split(':')[0],
        port=int(REDIS_URL.split(':')[1]),
        decode_responses=True,
        retry_on_timeout=True
    )
    logger.log(level=logging.INFO, msg="connected to redis for short term state")
except Exception as e:
    logger.log(level=logging.ERROR, msg=f"failed to connect to redis for short term state, error: {e}")

# --- Pinecone setup (Vector DB)

pc = retry_thing(lambda : Pinecone(api_key=VDB_KEY))()

# --- Langfuse setup
@retry_thing
def setup_langfuse():
    nest_asyncio.apply()
    OpenAIAgentsInstrumentor().instrument()
    return get_client()
 
langfuse = setup_langfuse()
# Verify connection
if langfuse.auth_check():
    logger.log(level=logging.INFO, msg="Langfuse client is authenticated and ready!")
else:
    logger.log(level=logging.ERROR, msg="Authentication failed. Please check your credentials and host.")


