import tkinter as tk
from tkinter import messagebox
from auth import login

# Function to handle login button click
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    
    result = login(username, password)
    if "✅" in result:
        messagebox.showinfo("Success", result)
    elif "🚨" in result or "🔒" in result:
        messagebox.showerror("Locked", result)
    else:
        messagebox.showerror("Error", result)

# Create GUI window
root = tk.Tk()
root.title("Intrusion Detection System")
root.geometry("400x250")

# Labels and Entry Fields
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=handle_login)
login_button.pack(pady=10)

# Run the GUI
root.mainloop()
