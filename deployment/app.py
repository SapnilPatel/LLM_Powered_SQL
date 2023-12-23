from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
# from few_shots import few_shots
import os
from dotenv import load_dotenv

load_dotenv()


def get_few_shot_db_chain():
    
    llm = GooglePalm(google_api_key=os.environ["api_key"],temperature=0.1)
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_name = "sapnil_tshirts"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)
    
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
to_vectorize = [" ".join(example.values()) for example in few_shots]
vectorstore = Chroma.from_texts(texts=to_vectorize,embedding=embeddings,metadatas=few_shots)
example_selector = SemanticSimilarityExampleSelector(vectorstore=vectorstore,k=2)

