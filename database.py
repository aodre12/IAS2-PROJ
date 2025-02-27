import sqlite3
import time

# Connect to the SQLite database
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    email TEXT UNIQUE,
                    password TEXT,
                    failed_attempts INTEGER DEFAULT 0,
                    locked_until REAL DEFAULT 0
                )''')
conn.commit()

# Function to add a user
def add_user(username, email, password):
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                       (username, email, password))
        conn.commit()
        return "✅ User registered successfully!"
    except sqlite3.IntegrityError:
        return "❌ Username or email already exists!"

# Function to get user data
def get_user(username):
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

# Function to update user data (for failed login attempts)
def update_user(username, failed_attempts, locked_until):
    cursor.execute("UPDATE users SET failed_attempts = ?, locked_until = ? WHERE username = ?", 
                   (failed_attempts, locked_until, username))
    conn.commit()
