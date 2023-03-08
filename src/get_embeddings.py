import openai
EMBEDDING_MODEL = "text-embedding-ada-002"

def get_embeddings(texts, model=EMBEDDING_MODEL):
  result = openai.Embedding.create(
    model=model,
    input=texts
  )
  return [result.embedding for result in result["data"]]