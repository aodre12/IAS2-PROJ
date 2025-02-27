import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    failed_attempts INTEGER DEFAULT 0,
                    locked_until REAL DEFAULT 0
                )''')
conn.commit()

# Function to add a new user (run once)
def add_default_user():
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
        conn.commit()

add_default_user()

# Function to get user data
def get_user(username):
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

# Function to update user data
def update_user(username, failed_attempts, locked_until):
    cursor.execute("UPDATE users SET failed_attempts = ?, locked_until = ? WHERE username = ?", 
                   (failed_attempts, locked_until, username))
    conn.commit()

# Close the database connection
def close_connection():
    conn.close()
