import tkinter as tk
from tkinter import messagebox
import time

# Store user credentials (for simplicity, using plaintext passwords)
users = {
    "admin": {"password": "password123", "failed_attempts": 0, "locked_until": 0}
}

# Track blocked users
blocked_ips = {}

# Simulating IP address
USER_IP = "192.168.1.100"

# Function to handle login attempts
def login():
    global USER_IP
    current_time = time.time()

    username = username_entry.get()
    password = password_entry.get()

    # Check if IP is blocked
    if USER_IP in blocked_ips and blocked_ips[USER_IP] > current_time:
        messagebox.showerror("Blocked", "🚫 Your IP is temporarily blocked!")
        return

    # Check if user exists
    if username not in users:
        messagebox.showerror("Error", "❌ User not found!")
        return

    user = users[username]

    # Check if account is locked
    if user["locked_until"] > current_time:
        messagebox.showwarning("Locked", "🔒 Account is locked! Try again later.")
        return

    # Validate password
    if password == user["password"]:
        user["failed_attempts"] = 0  # Reset failed attempts
        messagebox.showinfo("Success", "✅ Login successful!")
    else:
        user["failed_attempts"] += 1

        # Lock account after 5 failed attempts
        if user["failed_attempts"] >= 5:
            user["locked_until"] = current_time + 300  # Lock for 5 minutes
            blocked_ips[USER_IP] = current_time + 600  # Block IP for 10 minutes
            messagebox.showerror("Locked", "🚨 Too many failed attempts! Account locked for 5 minutes.")
            return

        messagebox.showerror("Error", "❌ Invalid password!")

# Create GUI window
root = tk.Tk()
root.title("Intrusion Detection System")
root.geometry("400x250")

# Labels and Entry Fields
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")  # Hide password
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Run the GUI
root.mainloop()
