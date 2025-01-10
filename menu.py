import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry("400x300")

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.master, text="Welcome to the Hospital Management System", font=("Helvetica", 16)).pack(pady=20)

        # Menu Options
        tk.Button(self.master, text="Manage Patients", command=self.manage_patients, width=30).pack(pady=10)
        tk.Button(self.master, text="Manage Appointments", command=self.manage_appointments, width=30).pack(pady=10)
        tk.Button(self.master, text="Manage Billing", command=self.manage_billing, width=30).pack(pady=10)
        tk.Button(self.master, text="Manage Inventory", command=self.manage_inventory, width=30).pack(pady=10)
        tk.Button(self.master, text="Exit", command=self.exit_program, width=30).pack(pady=10)

    def manage_patients(self):
        # Import and run the patient management module
        import patient_management
        patient_management.PatientManagement(tk.Toplevel(self.master))

    def manage_appointments(self):
        # Import and run the appointment management module
        import appointment_form
        appointment_form.AppointmentForm(tk.Toplevel(self.master))

    def manage_billing(self):
        # Import and run the billing management module
        import billing_form
        billing_form.BillingForm(tk.Toplevel(self.master))

    def manage_inventory(self):
        # Import and run the inventory management module
        import inventory_management
        inventory_management.InventoryManagement(tk.Toplevel(self.master))

    def exit_program(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()
