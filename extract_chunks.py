import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def chunk_text(text, chunk_size=50):
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    chunks = []
    current_chunk = []

    for line in lines:
        current_chunk.append(line)
        if len(current_chunk) >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# === USAGE ===
input_folder = "bj_data"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_folder, filename)
        print(f"Processing: {pdf_path}")
        text = extract_text_from_pdf(pdf_path)
        chunks = chunk_text(text)

        output_file = os.path.splitext(filename)[0] + "_clauses.txt"
        output_path = os.path.join(output_folder, output_file)

        with open(output_path, "w") as f:
            for c in chunks:
                f.write(c + "\n---\n")

        print(f"Saved chunks to: {output_path}")

