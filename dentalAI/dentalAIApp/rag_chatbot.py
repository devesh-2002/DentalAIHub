import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

load_dotenv()
os.environ['OPENAI_API_KEY'] = "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"

PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

def query_openai(input_text):
    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)
    return response
