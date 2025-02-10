# SQLite Chatbot

This project is a Python-based chatbot that interacts with an SQLite database to answer user queries about employees and departments.
## How It Works
- The assistant takes natural language queries from users.
- It converts the queries into SQL statements.
- It fetches the requested data from an SQLite database.
- It returns clear and formatted responses.

## Installation & Running Locally
1. Clone this repository: git clone https://github.com/akashchachere/sqlite-chatbot.git
   cd sqlite-chatbot
2. Install dependencies: pip install sqlite3
3. Set up the database: python setup_db.py
4. Run the chatbot: chatbot.py
   
## Example Usage
You: Show me all employees in the Sales department.
Chatbot: [(1, 'Alice', 'Sales', 50000, '2021-01-15')]

You: Who is the manager of the Engineering department?
Chatbot: [('Bob',)]
You: Bye
Chatbot: Goodbye!
## Output

1. Database Schemas
   
![Image](https://github.com/user-attachments/assets/a001c440-991c-41c5-bded-7d3435c638bb)

2. Query Output

![Image](https://github.com/user-attachments/assets/ccd6b2b2-cbe8-40ab-b206-07a98732bfa2)
