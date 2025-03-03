from fastapi import FastAPI, Query, HTTPException, File, UploadFile
import fastapi, io
from PyPDF2 import PdfReader
from .retrieve import search_chunks
from .chunk_store import store_text_in_db, split_text
from .llm_generation import generate_text, generate_text_replacement
from typing import Dict

app = FastAPI()
router = fastapi.APIRouter()

@router.post("/chat/")
async def chat(query: str = Query(..., description="User query for chatbot")) -> Dict[str, str]:
    """Process user query and return response based on stored document chunks."""
    relevant_chunks = search_chunks(query)

    if not relevant_chunks:
        return {"question": query, "answer": "No relevant information found in the uploaded documents."}
    
    answer = generate_text(data=",".join(text for text in relevant_chunks) )
    return {"question": query, "answer": str(answer)}

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)) -> Dict[str, str]:
    """Opens a PDF, reads the text and pass the extracted text to chunk and store it for retrieval."""
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # Read the file content
    file_content = await file.read()
    # Use PyPDF to extract text
    reader = PdfReader(io.BytesIO(file_content))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    chunk_ids, chunks = split_text (file.filename, text)
    # Store chunks in SQLite
    store_text_in_db(chunk_ids, chunks)
    return {"message" : "Document upload Success"}

