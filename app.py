import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "/data/test_users.db")

DB_NAME = "test_users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')
    # Skapa två testanvändare
    c.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (1, 'Peja', 'peja@test.se')")
    c.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (2, 'Matilda', 'matilda@test.se')")
    conn.commit()
    conn.close()

def display_users():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    print("Users in database:")
    for u in users:
        print(u)
    conn.close()

# GDPR-funktioner
def clear_test_data():
    """Rensar alla testanvändare (Right to be Forgotten)"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    print("All test data cleared.")

def anonymize_data():
    """Anonymiserar användardata"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET name='Anonym Användare', email='anonym@test.se'")
    conn.commit()
    conn.close()
    print("All data anonymized.")

if __name__ == "__main__":
    init_db()
    display_users()


