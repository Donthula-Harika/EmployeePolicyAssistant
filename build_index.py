from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import pickle

pdf_files = [
    "Employee Handbook.pdf",
    "Leave Policy.pdf",
    "Travel Policy.pdf",
    "Work From Home Policy.pdf",
    "Medical Insurance Policy.pdf"
]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = []

for file in pdf_files:
    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    pdf_chunks = splitter.split_text(text)

    # Keep source information
    for chunk in pdf_chunks:
        chunks.append({
            "source": file,
            "text": chunk
        })

print(f"Total chunks created: {len(chunks)}")

# Extract only text for embedding
texts = [chunk["text"] for chunk in chunks]

# Embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = model.encode(
    texts,
    convert_to_numpy=True
)

dimension = embeddings.shape[1]

# FAISS index
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    "faiss_index.bin"
)

with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Index created successfully!")