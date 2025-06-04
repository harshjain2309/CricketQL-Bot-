import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector, PromptTemplate, FewShotPromptTemplate
from few_shots import few_shots

load_dotenv()

def get_ipl_db_chain():
    db = SQLDatabase.from_uri(
        "mysql+pymysql://root:your_password@localhost/ipl_chatbot",
        sample_rows_in_table_info=3
    )

    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-instruct")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    texts = ["\n".join([v for v in shot.values()]) for shot in few_shots]
    vectorstore = Chroma.from_texts(texts, embeddings, metadatas=few_shots)

    selector = SemanticSimilarityExampleSelector(vectorstore=vectorstore, k=2)

    prefix = """You are a SQL expert for an IPL database.
Convert the question to SQL, run it, and return the final answer.
Use only SELECT queries. Use exact column/table names:
- matches(id, season, city, date, team1, team2, toss_winner, toss_decision, winner, result, result_margin, player_of_match, venue)
- deliveries(match_id, inning, batting_team, bowling_team, over, ball, batsman, bowler, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder)
"""

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=selector,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix="\nQuestion: {input}\nSQLQuery:",
        input_variables=["input", "table_info", "top_k"]
    )

    return SQLDatabaseChain.from_llm(llm, db, prompt=few_shot_prompt, verbose=True)