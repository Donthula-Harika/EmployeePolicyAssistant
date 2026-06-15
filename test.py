# Test the RAG pipeline
from rag_pipeline import answer_question

question = "How many casual leaves are available?"

response = answer_question(
    question
)

print(response)