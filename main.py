import fitz  # PyMuPDF for PDF text extraction
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify ["http://localhost"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample document database for comparison
DOCUMENTS_DB = {
    "original": """Artificial Intelligence (AI) is transforming industries by automating tasks, improving efficiency, 
    and enhancing decision-making. AI applications, including machine learning, are widely used across different fields."""
}

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    with fitz.open(pdf_path) as doc:
        text = "\n".join([page.get_text() for page in doc]).strip()
    return text

def check_plagiarism(new_text):
    """Check plagiarism using TF-IDF + Cosine Similarity"""
    corpus = list(DOCUMENTS_DB.values()) + [new_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    
    highest_match = max(similarity_scores)

    if highest_match > 0.2:
        return f"⚠️ Plagiarism Detected ({highest_match*100:.2f}% match with existing document)"

    return "✅ No Plagiarism Found"

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    """Upload a PDF, extract text, and check for plagiarism."""
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    extracted_text = extract_text_from_pdf(file_path)
    
    if not extracted_text:
        return {"error": "No text extracted from PDF. Try another file."}

    result = check_plagiarism(extracted_text)

    os.remove(file_path)

    return {"filename": file.filename, "result": result}

# Run server with: uvicorn main:app --reload
