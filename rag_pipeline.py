# Main RAG pipeline

from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
import faiss
import pickle

# 1. Load Embedding Model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



# 2. Load FAISS Index
index = faiss.read_index(
    "faiss_index.bin"
)


# 3. Load Chunks
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


# 4. Load LLM
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(
    model_name
)

llm = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto"
)


# 5. Answer Question
def answer_question(question):
    # Embed query
    query_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    )

    # Search FAISS
    distances, indices = index.search(
        query_embedding,
        k=3
    )

    # Retrieve top 3 chunks
    retrieved_chunks = []

    for i in indices[0]:

        if i < 0:
            continue

        chunk = chunks[i]

        retrieved_chunks.append(
            f"Source: {chunk['source']}\n"
            f"{chunk['text']}"
        )

    # Build context
    context = "\n\n".join(
        retrieved_chunks
    )

    # Debug: Show retrieved context
    print("\n===== RETRIEVED CONTEXT =====")
    print(context)
    print("=============================\n")


    # Create prompt
    prompt = f"""
You are an employee policy question-answering system.

Use ONLY the information in the context.

Answer ONLY the question asked.

Do NOT:
- answer another question
- create another Question/Answer pair
- repeat the prompt
- invent information
- confuse different policies
- add explanations that are not in the context

If the answer is present in the context, give the exact answer.

If the answer is not present, say:
The policy does not specify this.

Context:
{context}

Question:
{question}

Direct answer:
"""

    # Tokenize
    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    ).to(llm.device)

    # Generate answer
    output = llm.generate(
        **inputs,
        max_new_tokens=20,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    # Get only newly generated tokens
    input_length = inputs["input_ids"].shape[1]

    generated_tokens = output[0][input_length:]

    # Decode response
    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    ).strip()


    # Debug: Show raw model response
    print("\n===== RAW MODEL RESPONSE =====")
    print(repr(response))
    print("==============================\n")


    # Clean generated response
    
    # Remove anything after a new Question
    if "Question:" in response:
        response = response.split(
            "Question:"
        )[0]


    # Remove anything after another Q&A section
    if "\nQ:" in response:
        response = response.split(
            "\nQ:"
        )[0]


    if "\nQuestion" in response:
        response = response.split(
            "\nQuestion"
        )[0]


    # Remove Answer labels if generated
    if response.startswith("Answer:"):
        response = response[
            len("Answer:"):
        ].strip()


    if response.startswith("Direct answer:"):
        response = response[
            len("Direct answer:"):
        ].strip()


    response = response.strip()


    # Limit to two sentences

    sentences = response.split(".")

    clean_answer = ".".join(
        sentences[:2]
    ).strip()


    # Final fallback

    if not clean_answer:
        clean_answer = (
            "The policy does not specify this."
        )


    return clean_answer