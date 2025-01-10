import tkinter as tk
from tkinter import messagebox
import mysql.connector

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("300x200")

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Username
        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        # Password
        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        login_button = tk.Button(self.root, text="Login", command=self.login)
        login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Here you would add code to verify the credentials against the database
        # For now, just show a message
        messagebox.showinfo("Login Attempt", f"Attempting to log in as {username}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()
