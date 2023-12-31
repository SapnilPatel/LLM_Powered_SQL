# LLM Powered SQL Project
## Overview
* The LLM Powered SQL project leverages the power of the Google PaLM to create the SQL query from natural language.
* Leverage HuggingFace "all-MiniLM-L6-v2" model to create embeddings for SQL queries. These embeddings are stored in the ChromaDB Database, providing a powerful and efficient way to retrieve information based on semantic similarity.
* Used LangChain to make it.

## Features
**Embeddings Generation:** Utilizes the HuggingFace "all-MiniLM-L6-v2" model to generate embeddings for SQL queries.

**ChromaDB Database:** Stores the generated embeddings in the ChromaDB Database for efficient retrieval and querying.

**Streamlit Deployment:** The model is deployed using Streamlit, providing a user-friendly interface for interacting with the LLM-powered SQL capabilities.
