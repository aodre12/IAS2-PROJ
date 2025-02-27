import tkinter as tk
from tkinter import messagebox
from database import add_user

# Function to handle user registration
def register_user():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not username or not email or not password:
        messagebox.showerror("Error", "❌ All fields are required!")
        return

    result = add_user(username, email, password)
    if "✅" in result:
        messagebox.showinfo("Success", result)
        root.destroy()  # Close window after successful registration
    else:
        messagebox.showerror("Error", result)

# Create GUI window for user registration
root = tk.Tk()
root.title("User Registration")
root.geometry("400x300")

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

# Register Button
register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack(pady=10)

# Run the GUI
root.mainloop()
