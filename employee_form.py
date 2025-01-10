import tkinter as tk
from tkinter import messagebox
import mysql.connector

class EmployeeForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Form")
        self.root.geometry("400x300")

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Employee Name
        tk.Label(self.root, text="Employee Name").pack(pady=5)
        self.employee_name_entry = tk.Entry(self.root)
        self.employee_name_entry.pack(pady=5)

        # Employee ID
        tk.Label(self.root, text="Employee ID").pack(pady=5)
        self.employee_id_entry = tk.Entry(self.root)
        self.employee_id_entry.pack(pady=5)

        # Position
        tk.Label(self.root, text="Position").pack(pady=5)
        self.position_entry = tk.Entry(self.root)
        self.position_entry.pack(pady=5)

        # Submit Button
        submit_button = tk.Button(self.root, text="Submit Employee", command=self.submit_employee)
        submit_button.pack(pady=20)

    def submit_employee(self):
        employee_name = self.employee_name_entry.get()
        employee_id = self.employee_id_entry.get()
        position = self.position_entry.get()

        # Here you would add code to save the employee information to the database
        # For now, just show a message
        messagebox.showinfo("Employee Submitted", f"Employee {employee_name} with ID {employee_id} has been submitted as {position}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeForm(root)
    root.mainloop()
