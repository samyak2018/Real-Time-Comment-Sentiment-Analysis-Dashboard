import sqlite3

def connect_db():
    return sqlite3.connect("comments.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comment TEXT,
            sentiment TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_comment(comment, sentiment):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO comments (comment, sentiment) VALUES (?, ?)",
        (comment, sentiment)
    )
    conn.commit()
    conn.close()

def get_counts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sentiment, COUNT(*) FROM comments GROUP BY sentiment"
    )
    data = cursor.fetchall()
    conn.close()
    return data
