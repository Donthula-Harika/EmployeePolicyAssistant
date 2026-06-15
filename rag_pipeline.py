# Main RAG pipeline
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
import faiss
import pickle
import torch

# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Load FAISS index
index = faiss.read_index(
    "faiss_index.bin"
)

# Load chunks
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load LLM
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(
    model_name
)

llm = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto"
)

# Answer function
def answer_question(question):

    # Embed query
    query_embedding = embedding_model.encode(
        [question]
    )

    # Search FAISS
    distances, indices = index.search(
        query_embedding,
        k=1
    )

    # Retrieve chunk
    context = chunks[
        indices[0][0]
    ]

    # Create prompt
    prompt = f"""
    You are an Employee Policy Assistant.

    Use only the information provided in the context.

    Provide a concise answer in one or two sentences.

    Do not generate additional questions.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    # Tokenize
    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    ).to(llm.device)

    # Generate answer
    output = llm.generate(
        **inputs,
        max_new_tokens=50,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode response
    response = tokenizer.decode(
            output[0],
            skip_special_tokens=True
        )

    # Extract answer
    if "Answer:" in response:
        response = response.split("Answer:")[-1]

        # Remove additional questions
    if "Question:" in response:
        response = response.split("Question:")[0]

    response = response.strip()

    
    sentences = response.split(".")

    clean_answer = ".".join(sentences[:2]).strip()

    return clean_answer