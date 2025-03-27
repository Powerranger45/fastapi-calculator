from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Database setup function
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create table on startup
@app.on_event("startup")
def startup():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT,
            num1 INTEGER,
            num2 INTEGER,
            result INTEGER
        )
    """)
    conn.commit()
    conn.close()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Calculator API with Database!"}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    result = num1 + num2
    conn = get_db_connection()
    conn.execute("INSERT INTO calculations (operation, num1, num2, result) VALUES (?, ?, ?, ?)",
                 ("add", num1, num2, result))
    conn.commit()
    conn.close()
    return {"result": result}

@app.get("/subtract/{num1}/{num2}")
def subtract(num1: int, num2: int):
    result = num1 - num2
    conn = get_db_connection()
    conn.execute("INSERT INTO calculations (operation, num1, num2, result) VALUES (?, ?, ?, ?)",
                 ("subtract", num1, num2, result))
    conn.commit()
    conn.close()
    return {"result": result}

@app.get("/multiply/{num1}/{num2}")
def multiply(num1: int, num2: int):
    result = num1 * num2
    conn = get_db_connection()
    conn.execute("INSERT INTO calculations (operation, num1, num2, result) VALUES (?, ?, ?, ?)",
                 ("multiply", num1, num2, result))
    conn.commit()
    conn.close()
    return {"result": result}

@app.get("/history")
def get_history():
    conn = get_db_connection()
    calculations = conn.execute("SELECT * FROM calculations").fetchall()
    conn.close()
    return {"history": [dict(row) for row in calculations]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("apiserver:app", host="127.0.0.1", port=8000, reload=True)
