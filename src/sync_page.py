from transformers import GPT2TokenizerFast
import numpy as np
from nltk.tokenize import sent_tokenize
from get_embeddings import get_embeddings 

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

def sync_page(import_process_id, page_content, page_id, chat_id):
  contexts = get_contexts(page_content)
  embeddings = get_embeddings([context["text"] for context in contexts])
  for i, context in enumerate(contexts):
    save_context(context, page_id, chat_id)
    save_embedding(embeddings[i], page_id, chat_id)

  update_import_progress(import_process_id, page_id)

def get_contexts(page_content):
  contexts = []
  if count_tokens(page_content) > 1500:
    texts = split_long_text(page_content)
    for text in texts:
      if count_tokens(text) <= 40:
        continue
      
      contexts.append({
        "text": text,
        "tokens": count_tokens(text),
      })
  else:
    contexts.append({
      "text": page_content,
      "tokens": count_tokens(page_content),
    })

  return contexts

def save_context(context, page_id, chat_id):
  pass

def save_embedding(embedding, page_id, chat_id):
  pass

def update_import_progress(import_process_id, page_id):
  pass

def count_tokens(text):
  """count the number of tokens in a string"""
  return len(tokenizer.encode(text))

def split_long_text(text, max_tokens=1500):
  long_text_tokens = count_tokens(text)
  if long_text_tokens > max_tokens:
    sentences = sent_tokenize(text.replace("\n", " "))
    sections = []
    section = ""

    for i, sentence in enumerate(sentences):
      if section != "" and count_tokens(section + ". " + sentence + ".") > max_tokens:
        sections.append(section + ".")
        section = ""
      else:
        section += ". " + sentence if section != "" else sentence

    if section != "":
      sections.append(section + ".")

    return sections

  return [text]


