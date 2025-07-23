# AI-Agent-to-Answer-E-commerce-Data-Questions
# AI Agent for E-Commerce Data Queries

This project is an AI-powered assistant that answers natural language questions related to e-commerce product performance, using structured CSV datasets and SQLite.

##  Features
- Converts user questions to SQL (rule-based)
- Answers from a SQLite database
- Supports:
  - Total Sales
  - Return on Ad Spend (RoAS)
  - Highest CPC product

##  Files
- `load_data.py` — loads CSVs into `ecommerce.db`
- `query_agent.py` — main program to ask questions
- `llm_utils.py` — maps user questions to SQL queries
- `total_sales.csv`, `ad_metrics.csv`, `eligibility.csv` — source datasets

## How to Run
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
