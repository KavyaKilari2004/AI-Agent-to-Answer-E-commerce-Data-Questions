#  E-Commerce AI Agent: Natural Language to SQL

This project builds an **AI Agent** that answers natural language questions about e-commerce sales and ad performance using structured data stored in CSVs and SQLite. The system translates natural language into SQL queries using simple rule-based logic and fetches the answer from a local database.

> No internet or LLM needed — works 100% offline and is beginner-friendly.

---

## Features

- Ask questions in plain English like:
  - *"What is my total sales?"*
  - *"Calculate the RoAS"*
  - *"Which product had the highest CPC?"*
- Translates questions into SQL using rule-based matching
- Runs queries against an SQLite database built from CSV files
- Displays clean, readable answers
- Modular and easy to extend

---

## Folder Structure
ecommerce-ai-agent/
├── total_sales.csv # Product sales data
├── ad_metrics.csv # Ad metrics data
├── eligibility.csv # Eligibility flags
├── load_data.py # Loads CSV data into SQLite
├── llm_utils.py # Rule-based logic for SQL generation
├── query_agent.py # Main interface for asking questions
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignore venv, pycache, etc
##  How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-ai-agent.git
cd ecommerce-ai-agent
2. Install Python dependencies
pip install -r requirements.txt
3. Load data into SQLite
python load_data.py
This will create a file called ecommerce.db containing all 3 tables.
4. Start the agent and ask questions
python query_agent.py
Then type your question like:
What is my total sales?
SAMPLE OUTPUT:
Ask a question about your e-commerce data: What is my total sales?

Generated SQL:
SELECT SUM(total_sales) as total_sales FROM total_sales;

Answer:
total_sales
----------------
55896.01

DEMO VIDEO RECORDING:
https://drive.google.com/file/d/1Qdj1Ue_VNEQXJO6fGhbcPAw7LrPc8ep2/view?usp=sharing


AUTHOR
KAVYA KILARI
INTEGRATED MTECH SOFTWARE ENGINEERING-21MIS0497

