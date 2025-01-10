import tkinter as tk
from tkinter import messagebox
import mysql.connector

class BillingForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Form")
        self.root.geometry("400x300")

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Patient Name
        tk.Label(self.root, text="Patient Name").pack(pady=5)
        self.patient_name_entry = tk.Entry(self.root)
        self.patient_name_entry.pack(pady=5)

        # Billing Amount
        tk.Label(self.root, text="Billing Amount").pack(pady=5)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        # Payment Method
        tk.Label(self.root, text="Payment Method").pack(pady=5)
        self.payment_method_entry = tk.Entry(self.root)
        self.payment_method_entry.pack(pady=5)

        # Submit Button
        submit_button = tk.Button(self.root, text="Submit Billing", command=self.submit_billing)
        submit_button.pack(pady=20)

    def submit_billing(self):
        patient_name = self.patient_name_entry.get()
        billing_amount = self.amount_entry.get()
        payment_method = self.payment_method_entry.get()

        # Here you would add code to save the billing information to the database
        # For now, just show a message
        messagebox.showinfo("Billing Submitted", f"Billing for {patient_name} of amount {billing_amount} has been submitted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingForm(root)
    root.mainloop()
