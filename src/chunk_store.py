from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def  store_text_in_db(chunk_ids, chunks):

    os.makedirs("files", exist_ok=True)

    for i in range(len(chunks)):
        with open(f'{"files"}/chunk_{chunk_ids[i]}.txt', 'w', encoding='utf-8') as f:
            f.write(chunks[i])
            
def  split_text(file_name, input_text):
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = text_splitter.split_text(input_text)
    chunk_ids = [file_name+"_"+str(i) for i in range(len(chunks))]

    return chunk_ids, chunks
    