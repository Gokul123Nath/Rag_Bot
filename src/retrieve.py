from whoosh import index
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser
import os
from typing import List

# Define schema
schema = Schema(content=TEXT(stored=True))

# Create index
def create_index() -> 'index.Index':
    """
    Creates an index directory and returns an index object.

    Returns:
        index.Index: An instance of the created index.
    """
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
    ix = index.create_in("indexdir", schema)
    return ix

# Adding documents to index
def indexing_doc() -> 'index.Index':
    """
    Adds documents from the 'files' directory to the index.

    Returns:
        index.Index: An instance of the updated index.
    """
    ix = create_index()
    writer = ix.writer()
    for chunk_file in os.listdir('files'):
        with open(f'files/{chunk_file}', 'r') as f:
            content = f.read()
            writer.add_document(content=content)
    writer.commit()
    return ix

def search_chunks(query_str) -> List[str]:
    """
    Searches for relevant chunks in the indexed documents based on the query string.

    Args:
        query_str (str): The search query string.

    Returns:
        List[str]: A list of relevant document chunk contents.
    """
    ix = indexing_doc()
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query)
        data = [result["content"] for result in results]
        return data
    