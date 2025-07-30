from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np

# Load sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("index_data/clauses.index")

# Load chunk data
with open("index_data/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

def search(query, top_k=3):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)
    return [(chunks[i], float(D[0][idx])) for idx, i in enumerate(I[0])]

# === USAGE EXAMPLE ===
if __name__ == "__main__":
    query = "46-year-old man, knee surgery, 3-month-old policy"
    results = search(query, top_k=3)

    print("Top Matching Clauses:\n")
    for i, (text, score) in enumerate(results):
        print(f"[{i+1}] (Distance: {score:.4f})")
        print(text)
        print("---")

