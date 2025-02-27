import tkinter as tk
from tkinter import messagebox
from database import add_user, get_user, update_user
import time

# Function to handle login
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    current_time = time.time()

    user = get_user(username)
    
    if not user:
        messagebox.showerror("Error", "❌ User not found!")
        return

    user_id, db_username, db_email, db_password, failed_attempts, locked_until = user

    # Check if the account is locked
    if locked_until > current_time:
        messagebox.showerror("Locked", "🔒 Account locked! Try again later.")
        return

    # Validate password
    if password == db_password:
        update_user(username, 0, 0)  # Reset failed attempts
        messagebox.showinfo("Success", "✅ Login successful!")
    else:
        failed_attempts += 1
        if failed_attempts >= 5:
            lock_time = current_time + 300  # Lock for 5 minutes
            update_user(username, failed_attempts, lock_time)
            messagebox.showerror("Locked", "🚨 Too many failed attempts! Account locked for 5 minutes.")
        else:
            update_user(username, failed_attempts, locked_until)
            messagebox.showerror("Error", "❌ Invalid password!")

# Function to handle registration
def handle_register():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not username or not email or not password:
        messagebox.showerror("Error", "❌ All fields are required!")
        return

    result = add_user(username, email, password)
    if "✅" in result:
        messagebox.showinfo("Success", result)
    else:
        messagebox.showerror("Error", result)

# Create GUI window
root = tk.Tk()
root.title("Intrusion Detection System")
root.geometry("400x350")

# Labels and Entry Fields
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Buttons for Login and Register
login_button = tk.Button(root, text="Login", command=handle_login)
login_button.pack(pady=5)

register_button = tk.Button(root, text="Register", command=handle_register)
register_button.pack(pady=5)

# Run the GUI
root.mainloop()
