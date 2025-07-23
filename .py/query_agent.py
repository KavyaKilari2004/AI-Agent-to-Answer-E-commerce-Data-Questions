import sqlite3
from llm_utils import question_to_sql

DB_PATH = "ecommerce.db"

def run_sql(sql):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        return rows, columns, None
    except Exception as e:
        return None, None, str(e)
    finally:
        conn.close()

def print_result(rows, columns):
    if not rows:
        print("(No results found)")
        return
    print(" | ".join(columns))
    print("-" * (len(" | ".join(columns)) + 5))
    for row in rows:
        print(" | ".join(str(val) for val in row))

def answer_question(question):
    sql = question_to_sql(question)
    print(f"\nGenerated SQL:\n{sql}\n")

    if sql.startswith("ERROR"):
        print(sql)
        return

    rows, columns, error = run_sql(sql)
    if error:
        print(f"SQL Error: {error}")
    else:
        print("Answer:")
        print_result(rows, columns)

if __name__ == "__main__":
    q = input("Ask a question about your e-commerce data: ")
    answer_question(q)
