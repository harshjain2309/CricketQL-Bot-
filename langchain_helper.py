# langchain_helper.py

import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate

load_dotenv()

def get_ipl_db_chain():
    # 1) Connect to the IPL MySQL database
    db = SQLDatabase.from_uri("mysql+pymysql://root:Harsh_jain%4009876@localhost/ipl_chatbot")

    # 2) Instantiate the Ollama LLM (Llama 2, temperature=0 for deterministic SQL)
    llm = Ollama(model="llama2", temperature=0)

    # 3) Build a PromptTemplate forcing ONLY a valid SELECT statement (no extra text)
    prefix = """You are a SQL expert for an IPL database.
Convert the user question into a valid MySQL SELECT query only.
Do NOT include any explanation, markdown, or extra text—output exactly one SELECT statement.
Use these exact tables and columns:

- matches(id, season, city, date, team1, team2, toss_winner, toss_decision, winner, result, result_margin, player_of_match, venue)
- deliveries(match_id, inning, batting_team, bowling_team, over, ball, batsman, bowler, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder)
"""

    suffix = "\nQuestion: {input}\nSQLQuery (only the SQL statement, no explanation or commentary):"

    prompt_template = PromptTemplate(
        input_variables=["input"],
        template=prefix + suffix
    )

    # 4) Create the SQLDatabaseChain. NOTE: pass (llm, db) positionally.
    chain = SQLDatabaseChain.from_llm(
        llm,                # first positional: the LLM
        db,                 # second positional: the SQLDatabase instance
        prompt=prompt_template,
        verbose=True,
        return_intermediate_steps=True
    )

    return chain
