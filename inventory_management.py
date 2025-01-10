import tkinter as tk
from tkinter import messagebox
import mysql.connector

class InventoryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")
        self.master.geometry("600x400")

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Item ID
        tk.Label(self.master, text="Item ID").grid(row=0, column=0, padx=10, pady=10)
        self.item_id_entry = tk.Entry(self.master)
        self.item_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Item Name
        tk.Label(self.master, text="Item Name").grid(row=1, column=0, padx=10, pady=10)
        self.item_name_entry = tk.Entry(self.master)
        self.item_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Quantity
        tk.Label(self.master, text="Quantity").grid(row=2, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(self.master)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10)

        # Supplier
        tk.Label(self.master, text="Supplier").grid(row=3, column=0, padx=10, pady=10)
        self.supplier_entry = tk.Entry(self.master)
        self.supplier_entry.grid(row=3, column=1, padx=10, pady=10)

        # Submit Button
        submit_button = tk.Button(self.master, text="Add Item", command=self.add_item)
        submit_button.grid(row=4, column=0, columnspan=2, pady=20)

    def add_item(self):
        item_id = self.item_id_entry.get()
        item_name = self.item_name_entry.get()
        quantity = self.quantity_entry.get()
        supplier = self.supplier_entry.get()

        # Database connection
        conn = mysql.connector.connect(
            host="localhost",
            user="dkb096",
            password="subzero",
            database="hospital"
        )
        cursor = conn.cursor()

        # Insert inventory record into the database
        cursor.execute('INSERT INTO INVENTORY (ITEM_ID, ITEM_NAME, QUANTITY, SUPPLIER) VALUES (%s, %s, %s, %s)', 
                       (item_id, item_name, quantity, supplier))
        conn.commit()
        messagebox.showinfo("Success", "Item added successfully!")

        # Clear the input fields
        self.clear_fields()

        # Close the database connection
        cursor.close()
        conn.close()

    def clear_fields(self):
        self.item_id_entry.delete(0, 'end')
        self.item_name_entry.delete(0, 'end')
        self.quantity_entry.delete(0, 'end')
        self.supplier_entry.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagement(root)
    root.mainloop()
