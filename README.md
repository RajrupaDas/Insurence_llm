# ClauseWise: LLM-Based Policy Query API

## Overview
ClauseWise is an API service that processes natural language insurance or policy-related queries, retrieves relevant clauses from unstructured documents, and returns structured JSON decisions with explanations.

---

## Features
- Parses user queries in plain English.
- Searches policy documents semantically using embeddings + FAISS.
- Provides approval/rejection decisions with clause-based justifications.
- Simple REST API built with FastAPI.

---

## Tech Stack
- Python 3.8+
- FastAPI
- SentenceTransformers (`all-MiniLM-L6-v2`)
- FAISS for vector similarity search
- PyMuPDF for PDF parsing
- (Optional) OpenAI API for decision reasoning OR mock rule-based logic

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-folder>
2. Create a Python virtual environment (recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not provided, install manually:

bash
Copy
Edit
pip install fastapi uvicorn sentence-transformers faiss-cpu pymupdf openai
4. Add your policy documents
Place your PDF files inside the data/ folder (e.g., data/policy_sample.pdf).

5. Build the clause index
Run the script to extract and embed clauses:

bash
Copy
Edit
python extract_chunks.py
python build_index.py
6. (Optional) Set OpenAI API key
If using OpenAI for decision making, set your API key as an environment variable:

bash
Copy
Edit
export OPENAI_API_KEY="your_api_key"     # Linux/macOS
set OPENAI_API_KEY="your_api_key"        # Windows
7. Run the FastAPI server
bash
Copy
Edit
python main.py
8. Test the API
Open your browser at:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
Use the /query POST endpoint to submit queries and receive JSON responses.
