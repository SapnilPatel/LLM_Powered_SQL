# LLM Powered SQL Project
## Overview
* Developed an LLM-powered SQL query generation system using Google PaLM to translate natural language into SQL queries.
* Integrated Hugging Face’s all-MiniLM-L6-v2 model to generate semantic embeddings of SQL queries, storing them in ChromaDB for fast and accurate retrieval based on semantic similarity.
* Employed LangChain to build a modular and scalable pipeline for query generation and retrieval.

## Features
**Embeddings Generation:** Utilizes the HuggingFace "all-MiniLM-L6-v2" model to generate embeddings for SQL queries.

**ChromaDB Database:** Stores the generated embeddings in the ChromaDB Database for efficient retrieval and querying.

**Streamlit Deployment:** The model is deployed using Streamlit, providing a user-friendly interface for interacting with the LLM-powered SQL capabilities.
