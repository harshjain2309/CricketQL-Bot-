
# 🏏 CricketQL Bot

CricketQL Bot is an intelligent GenAI-powered chatbot that allows you to ask natural language questions about IPL cricket matches — and get accurate answers using live SQL queries on a structured IPL database.

Built with [LangChain](https://www.langchain.com/), OpenAI, and MySQL, this project bridges the gap between human queries and structured cricket data.

---

## 🚀 Features

- 💬 Ask IPL-related questions in plain English  
- 🧠 Automatic SQL query generation using LLMs  
- 📊 Real-time execution on a MySQL cricket database  
- ⚡ Fast, accurate answers from structured `matches` and `deliveries` data  
- ✅ Powered by LangChain + OpenAI (or Google PaLM)  

---

## 📂 Dataset Used

- `matches_cleaned.csv` – Match metadata (teams, venue, result, etc.)  
- `deliveries_cleaned.csv` – Ball-by-ball delivery data for every IPL game  

---

## 🔧 Technologies Used

| Tech                             | Purpose                                  |
|----------------------------------|------------------------------------------|
| Python                           | Core scripting language                  |
| Streamlit                        | Front-end chatbot UI                     |
| MySQL                            | Backend database engine                  |
| LangChain                        | Prompt engineering and chaining          |
| OpenAI / LLM                     | SQL query generation                     |
| ChromaDB                         | Vector storage for few-shot examples     |
| HuggingFace Sentence Transformers| Embeddings for similarity search         |

---

## 💻 How It Works

1. User enters a question (e.g. _"Who scored the most runs in 2020?"_)  
2. LangChain retrieves similar few-shot examples  
3. LLM generates an appropriate SQL query  
4. Query runs on a MySQL database containing IPL data  
5. SQL result is transformed into a natural language answer  

---

## 📸 Screenshots

![CricketQL Bot Demo](docs/demo.gif)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/harshjain2309/CricketQL-Bot.git
cd CricketQL-Bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare MySQL Database

Open MySQL and run `ipl.sql`:

```bash
mysql -u root -p < ipl.sql
```

Make sure your `.env` file contains:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the App

```bash
streamlit run main.py
```

---

## 🔍 Sample Questions You Can Ask

- Who won the most matches in 2019?  
- How many runs did Virat Kohli score in match 392201?  
- Which bowler took the most wickets in 2020?  
- How many sixes were hit in the 2018 season?  

---

## 🧠 Inspiration

This project is inspired by GenAI + SQL-based assistants like the **T-shirt Retail LLM project**, adapted for IPL match analytics. It’s a great example of combining:

- RAG (Retrieval Augmented Generation)  
- Few-shot prompting  
- SQL databases with LLMs  

---

## 📘 License

MIT License.  
Feel free to fork, learn from, and build upon CricketQL Bot!  

---

## 🙋‍♂️ Author

Made by **Harsh Jain**  
