import sqlite3
from contextlib import contextmanager
from typing import List, Dict

DATABASE_PATH = "patients.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    """Initialize database schema"""
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                last_visit DATE,
                status TEXT
            )
        """)

def get_total_patients() -> int:
    """Get total number of registered patients"""
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT COUNT(*) FROM patients")
        return cursor.fetchone()[0]

def get_today_appointments() -> int:
    """Get today's appointments count"""
    today = datetime.date.today().isoformat()
    with get_db_connection() as conn:
        cursor = conn.execute("""
            SELECT COUNT(*) FROM appointments
            WHERE date = ?
        """, (today,))
        return cursor.fetchone()[0]

# Initialize database on first import
init_db()