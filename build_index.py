from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

# Load all chunked .txt files from output/
all_chunks = []
input_folder = "output"

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(input_folder, filename), "r") as f:
            raw = f.read()
        chunks = [c.strip() for c in raw.split("\n---\n") if c.strip()]
        all_chunks.extend(chunks)

print(f"Total chunks loaded: {len(all_chunks)}")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(all_chunks)

# Build FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))

# Save index and chunks
os.makedirs("index_data", exist_ok=True)
faiss.write_index(index, "index_data/clauses.index")

with open("index_data/chunks.pkl", "wb") as f:
    pickle.dump(all_chunks, f)

print("Index and chunks saved successfully.")

