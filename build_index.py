# Build FAISS index from PDFs
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

all_text = ""

for file in pdf_files:
    reader = PdfReader(file)

    for page in reader.pages:
        all_text += page.extract_text() + "\n"

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(all_text)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, "faiss_index.bin")

with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Index created successfully!")