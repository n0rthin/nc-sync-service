
from .main_service import update_import_progress
from .embeddings import get_embeddings, save_embeddings, clear_embeddings
from .context import get_contexts, clear_contexts, save_context


def sync_page(import_process_id, page_content, user_id, page_id, chat_id):
  print(f"process: {import_process_id}, clearing embeddings for page: {page_id}")
  clear_embeddings(page_id)
  print(f"process: {import_process_id}, clearing contexts for page: {page_id}")
  clear_contexts(page_id)
  print(f"process: {import_process_id}, getting contexts for page: {page_id}")
  contexts = get_contexts(page_content)
  print(f"process: {import_process_id}, getting embeddings for page: {page_id}")
  embeddings = get_embeddings([context["text"] for context in contexts])
  context_ids = []
  print(f"process: {import_process_id}, saving contexts for page: {page_id}")
  for i, context in enumerate(contexts):
    context_id = save_context(context, user_id, page_id, i)
    context_ids.append(context_id)

  print(f"process: {import_process_id}, saving embeddings for page: {page_id}")
  save_embeddings(list(zip(embeddings, context_ids)), user_id, chat_id, page_id)
  print(f"process: {import_process_id}, updating sync progress for page: {page_id}")
  update_import_progress(import_process_id, page_id)


