from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load local embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Store texts globally (simple version)
documents = []
index = None


def create_vectorstore():
    global documents, index

    with open("data/sample.txt", "r") as file:
        text = file.read()

    # Split into chunks (simple split)
    documents = text.split("\n")

    # Convert to embeddings
    embeddings = model.encode(documents)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))


def search_vectorstore(query):
    global index, documents

    query_embedding = model.encode([query])

    D, I = index.search(np.array(query_embedding), k=2)

    results = [documents[i] for i in I[0]]
    return " ".join(results)