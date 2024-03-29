
from nltk.tokenize import sent_tokenize
from . import db
from transformers import GPT2TokenizerFast
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

def get_contexts(page_content):
  contexts = []
  if count_tokens(page_content) > 1500:
    texts = split_long_text(page_content)
    for text in texts:
      if count_tokens(text) <= 10:
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

def save_context(context, user_id, page_id, context_index):
  db.cursor.execute(f"""
  INSERT INTO contexts 
  (user_id, page_id, content, index, tokens) 
  VALUES (%s, %s, %s, %s, %s)
  RETURNING id;
  """, (user_id, page_id, context["text"], context_index, context["tokens"]))
  db.conn.commit()
  return db.cursor.fetchone()[0]

def clear_contexts(page_id):
  db.cursor.execute(f"""
  DELETE FROM contexts WHERE page_id = %s;
  """, (page_id,))
  db.conn.commit()

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
