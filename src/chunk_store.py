from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from typing import List, Tuple
from .logger import get_logger

logger = get_logger("RAG Bot")


def  store_text_in_db(chunk_ids: List[str], chunks: List[str]) -> None:
    """
    Stores text chunks in individual files within the 'files' directory.

    Args:
        chunk_ids (list): A list of unique identifiers for each text chunk.
        chunks (list): A list of text chunks to be stored.

    Creates a directory named 'files' if it doesn't exist and writes each text chunk to a separate file
    with the corresponding chunk ID as the filename.
    """
    try :
        os.makedirs("files", exist_ok=True)
        for i in range(len(chunks)):
            with open(f'{"files"}/chunk_{chunk_ids[i]}.txt', 'w', encoding='utf-8') as f:
                f.write(chunks[i])
        logger.info("Chunks Stored successfully")

    except Exception as e:
        logger.error(f"Error while storing chunks : {e}")
            
def  split_text(file_name: str, input_text: str) -> Tuple[List[str], List[str]]:
    """
    Splits input text into chunks and generates unique identifiers for each chunk.

    Args:
        file_name (str): The base name to be used for generating chunk IDs.
        input_text (str): The input text to be split into chunks.

    Returns:
        tuple: A tuple containing two lists:
            chunk_ids (list): A list of unique identifiers for each text chunk.
            chunks (list): A list of text chunks.
    """   
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        chunks = text_splitter.split_text(input_text)
        chunk_ids = [file_name+"_"+str(i) for i in range(len(chunks))]
        logger.info("Text splitting successful")
        return chunk_ids, chunks
    
    except Exception as e:
        logger.error (f"Error on splitting text : {e}")
    