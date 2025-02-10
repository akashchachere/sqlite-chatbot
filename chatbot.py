from flask import Flask, request, jsonify, render_template
import sqlite3
import re

app = Flask(__name__)


# Function to create a database connection
def create_connection():
    return sqlite3.connect("company.db")


# Function to convert natural language queries into SQL
def process_query(user_input):
    user_input = user_input.lower()

    # Query to fetch all employees from a department
    match = re.search(r"all employees in the (\w+) department", user_input)
    if match:
        department = match.group(1).capitalize()
        return "SELECT * FROM Employees WHERE Department=?", (department,)

    # Query to get the manager of a department
    match = re.search(r"manager of the (\w+) department", user_input)
    if match:
        department = match.group(1).capitalize()
        return "SELECT Manager FROM Departments WHERE Name=?", (department,)

    # Query to list employees hired after a date
    match = re.search(r"employees hired after (\d{4}-\d{2}-\d{2})", user_input)
    if match:
        date = match.group(1)
        return "SELECT * FROM Employees WHERE Hire_Date > ?", (date,)

    # Query to get total salary expense for a department
    match = re.search(r"total salary expense for the (\w+) department", user_input)
    if match:
        department = match.group(1).capitalize()
        return "SELECT SUM(Salary) FROM Employees WHERE Department=?", (department,)

    return None, None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query():
    user_input = request.json.get("message")
    sql_query, params = process_query(user_input)

    if not sql_query:
        return jsonify({"response": "Sorry, I couldn't understand that query."})

    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query, params)
        results = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        if not results:
            response = "No results found."
        else:
            response = "\n".join([" ".join(map(str, row)) for row in results])  # Removes quotes and separators

        return jsonify({"response": response})

    except sqlite3.Error as e:
        return jsonify({"response": f"Error: {str(e)}"})

    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)
