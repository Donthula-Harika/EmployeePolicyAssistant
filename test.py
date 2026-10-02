from rag_pipeline import answer_question

question = "How many casual leaves are available?"

answer = answer_question(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)