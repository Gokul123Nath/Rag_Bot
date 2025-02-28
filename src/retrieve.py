from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser
import os

# Define schema
schema = Schema(content=TEXT(stored=True))

# Create index
def create_index():
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
    ix = create_in("indexdir", schema)
    return ix

# Adding documents to index
def indexing_doc():
    ix = create_index()
    writer = ix.writer()
    for chunk_file in os.listdir('files'):
        with open(f'files/{chunk_file}', 'r') as f:
            content = f.read()
            writer.add_document(content=content)
    writer.commit()
    return ix

def search_chunks(query_str):

    ix = indexing_doc()
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query)

        data = [result["content"] for result in results]

        return data
    