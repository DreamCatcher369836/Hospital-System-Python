import tkinter as tk
from tkinter import messagebox
import mysql.connector

class AppointmentForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Schedule Appointment")
        self.root.geometry("400x300")

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Patient Name
        tk.Label(self.root, text="Patient Name").pack(pady=5)
        self.patient_name_entry = tk.Entry(self.root)
        self.patient_name_entry.pack(pady=5)

        # Appointment Date
        tk.Label(self.root, text="Appointment Date").pack(pady=5)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack(pady=5)

        # Appointment Time
        tk.Label(self.root, text="Appointment Time").pack(pady=5)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack(pady=5)

        # Submit Button
        submit_button = tk.Button(self.root, text="Schedule Appointment", command=self.schedule_appointment)
        submit_button.pack(pady=20)

    def schedule_appointment(self):
        patient_name = self.patient_name_entry.get()
        appointment_date = self.date_entry.get()
        appointment_time = self.time_entry.get()

        # Here you would add code to save the appointment to the database
        # For now, just show a message
        messagebox.showinfo("Appointment Scheduled", f"Appointment for {patient_name} on {appointment_date} at {appointment_time} has been scheduled.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentForm(root)
    root.mainloop()
