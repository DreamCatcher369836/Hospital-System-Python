import tkinter as tk
from tkinter import messagebox
import mysql.connector

class PatientManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Management System")
        self.master.geometry("600x400")

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Patient ID
        tk.Label(self.master, text="Patient ID").grid(row=0, column=0, padx=10, pady=10)
        self.patient_id_entry = tk.Entry(self.master)
        self.patient_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Patient Name
        tk.Label(self.master, text="Patient Name").grid(row=1, column=0, padx=10, pady=10)
        self.patient_name_entry = tk.Entry(self.master)
        self.patient_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Age
        tk.Label(self.master, text="Age").grid(row=2, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)

        # Contact
        tk.Label(self.master, text="Contact").grid(row=3, column=0, padx=10, pady=10)
        self.contact_entry = tk.Entry(self.master)
        self.contact_entry.grid(row=3, column=1, padx=10, pady=10)

        # Submit Button
        submit_button = tk.Button(self.master, text="Add Patient", command=self.add_patient)
        submit_button.grid(row=4, column=0, columnspan=2, pady=20)

    def add_patient(self):
        patient_id = self.patient_id_entry.get()
        patient_name = self.patient_name_entry.get()
        age = self.age_entry.get()
        contact = self.contact_entry.get()

        # Database connection
        conn = mysql.connector.connect(
            host="localhost",
            user="dkb096",
            password="subzero",
            database="hospital_management"
        )
        cursor = conn.cursor()

        # Insert patient record into the database
        cursor.execute('INSERT INTO PATIENT (PATIENT_ID, NAME, AGE, CONTACT) VALUES (%s, %s, %s, %s)', 
                       (patient_id, patient_name, age, contact))
        conn.commit()
        messagebox.showinfo("Success", "Patient added successfully!")

        # Clear the input fields
        self.clear_fields()

        # Close the database connection
        cursor.close()
        conn.close()

    def clear_fields(self):
        self.patient_id_entry.delete(0, 'end')
        self.patient_name_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.contact_entry.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientManagement(root)
    root.mainloop()
