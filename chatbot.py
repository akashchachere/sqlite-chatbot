from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def query_database(sql_query):
    """Function to query SQLite database and return results."""
    conn = sqlite3.connect("company.db")  # Your SQLite database file
    cursor = conn.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route("/chat", methods=["GET"])
def chat():
    """Endpoint to handle chat queries."""
    user_query = request.args.get("query", "")
    
    if "employees in" in user_query.lower():
        dept = user_query.split("in")[-1].strip()
        sql_query = f"SELECT Name FROM Employees WHERE Department='{dept}'"
    elif "manager of" in user_query.lower():
        dept = user_query.split("of")[-1].strip()
        sql_query = f"SELECT Manager FROM Departments WHERE Name='{dept}'"
    else:
        return jsonify({"response": "Sorry, I don't understand your query."})
    
    results = query_database(sql_query)
    return jsonify({"response": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
