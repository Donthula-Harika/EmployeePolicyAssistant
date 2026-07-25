# Employee Policy Assistant

A simple Retrieval-Augmented Generation (RAG) application that answers employee-policy questions from local PDF documents. It retrieves the most relevant policy text with semantic search, then asks a language model to produce a concise, context-based answer.

## Features

- Reads employee-policy PDFs, including leave, travel, work-from-home, handbook, and medical-insurance policies.
- Splits extracted text into chunks and creates embeddings with `all-MiniLM-L6-v2`.
- Stores and searches embeddings locally with FAISS.
- Generates answers with `TinyLlama-1.1B-Chat-v1.0`.
- Provides a Streamlit user interface for asking questions.

## Tech stack

Python, Streamlit, Sentence Transformers, FAISS, Hugging Face Transformers, PyTorch, PyPDF, and LangChain text splitters.

## Project structure

```text
app.py              Streamlit interface
rag_pipeline.py     Retrieval and answer-generation pipeline
build_index.py      Extracts PDFs and creates the FAISS index
create_pdfs.py      Creates the included sample policy PDFs
test.py             Simple command-line pipeline test
requirements.txt    Python dependencies
```

## Setup

Prerequisites: Python 3.10 or later and an internet connection the first time the embedding and language models are downloaded.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, run this once for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Build the knowledge index

The repository includes sample policy PDFs. To recreate them and rebuild the retrieval index, run:

```powershell
python create_pdfs.py
python build_index.py
```

This generates `faiss_index.bin` and `chunks.pkl`, which are required by the application.

## Run the application

```powershell
streamlit run app.py
```

Open the local URL printed by Streamlit and ask a policy question, for example: `How many casual leaves are available?`

To test the pipeline without the web interface:

```powershell
python test.py
```

## How it works

```text
Policy PDFs -> text chunks -> embeddings -> FAISS index
User question -> query embedding -> closest policy chunk -> TinyLlama -> answer
```

## Current limitations

- This is a learning/demo project, not a production HR-policy system.
- Retrieval currently returns only one text chunk per question.
- Models load locally and can make initial startup slow.
- The answer model should be evaluated and guarded further before use with real company policies.

## Resume description

Built a RAG-based Employee Policy Assistant using Python, Streamlit, Sentence Transformers, FAISS, and TinyLlama to retrieve information from PDF policy documents and generate context-grounded answers.
