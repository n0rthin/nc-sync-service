import openai
import pinecone
import os
from tenacity import (
  retry,
  stop_after_attempt,
  wait_random_exponential,
) 

EMBEDDING_MODEL = "text-embedding-ada-002"

pinecone.init(api_key=os.environ["PINECONE_API_KEY"], environment=os.environ["PINECONE_ENV"])
index = pinecone.Index(os.environ["PINECONE_INDEX_NAME"])

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(7))
def get_embeddings(texts, model=EMBEDDING_MODEL):
  result = openai.Embedding.create(
    model=model,
    input=texts
  )
  return [result.embedding for result in result["data"]]

def save_embeddings(embeddings, user_id, chat_id, page_id):
  vectors = [{
    "id": str(context_id),
    "values": embedding,
    "metadata": {'chat_id': chat_id, 'page_id': page_id, "context_id": context_id}
  } for embedding, context_id in embeddings]
  index.upsert(
    vectors=vectors,
    namespace=str(user_id)
  )