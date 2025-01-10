import tkinter as tk
from tkinter import messagebox
import mysql.connector

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # Database connection
        self.db_connection = self.connect_to_database()

        # Create UI components
        self.create_widgets()

        # Create menu bar
        self.create_menu()

    def connect_to_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="your_username",
                password="your_password",
                database="hospital_db"
            )
            return connection
        except mysql.connector.Error as err:
            messagebox.showerror("Database Connection Error", str(err))
            return None

    def create_widgets(self):
        # Example label
        label = tk.Label(self.root, text="Welcome to the Hospital Management System", font=("Arial", 16))
        label.pack(pady=20)

        # Example button
        button = tk.Button(self.root, text="Exit", command=self.root.quit)
        button.pack(pady=10)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # Patient Management Menu
        patient_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Patient Management", menu=patient_menu)
        patient_menu.add_command(label="Add Patient")
        patient_menu.add_command(label="View Patients")

        # Appointment Scheduling Menu
        appointment_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Appointment Scheduling", menu=appointment_menu)
        appointment_menu.add_command(label="Schedule Appointment")
        appointment_menu.add_command(label="View Appointments")

        self.root.config(menu=menu_bar)

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()
