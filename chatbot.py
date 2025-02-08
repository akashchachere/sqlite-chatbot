import sqlite3
import re

def create_connection():
    return sqlite3.connect("company.db")


# Function to convert natural language queries into SQL
def process_query(user_input):
    user_input = user_input.lower()

    # Query to fetch all employees from a department
    match = re.search(r"all employees in the (\w+) department", user_input)
    if match:
        department = match.group(1).capitalize()
        return f"SELECT * FROM Employees WHERE Department='{department}';"

    # Query to get the manager of a department
    match = re.search(r"manager of the (\w+) department", user_input)
    if match:
        department = match.group(1).capitalize()
        return f"SELECT Manager FROM Departments WHERE Name='{department}';"

    # Query to list employees hired after a date
    match = re.search(r"employees hired after (\d{4}-\d{2}-\d{2})", user_input)
    if match:
        date = match.group(1)
        return f"SELECT * FROM Employees WHERE Hire_Date > '{date}';"

    # Query to get total salary expense for a department
    match = re.search(r"total salary expense for the (\w+) department", user_input)
    if match:
        department = match.group(1).capitalize()
        return f"SELECT SUM(Salary) FROM Employees WHERE Department='{department}';"

    return None


def chat_bot():
    print("Hello! I am your SQLite chat assistant. Ask me about employees and departments.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        sql_query = process_query(user_input)
        if not sql_query:
            print("Chatbot: Sorry, I couldn't understand that query.")
            continue

        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql_query)
            results = cursor.fetchall()
            if not results:
                print("Chatbot: No results found.")
            else:
                print("Chatbot:", results)
        except sqlite3.Error as e:
            print("Chatbot: Error -", str(e))
        finally:
            conn.close()


if __name__ == "__main__":
    chat_bot()
