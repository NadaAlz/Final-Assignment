import tkinter as tk
from tkinter import messagebox
from enum import Enum
import re
class S_Type(Enum): 
    C = "Catering"
    CL = "Cleaning"
    F = "Furniture"
    D = "Decorations"
    E = "Entertainment"

class Supplier:
    """Class to represent a supplier"""
    def __init__(self, s_name='', s_ID='', s_type=S_Type.C, s_address='', s_contact_details=''):
        self.s_name = s_name
        self.s_ID = s_ID
        self.s_type = s_type
        self.s_address = s_address
        self.s_contact_details = s_contact_details

    def set_s_name(self, s_name):
        self.s_name = s_name

    def set_s_ID(self, s_ID):
        self.s_ID = s_ID

    def set_s_type(self, s_type):
        self.s_type = s_type

    def set_s_address(self, s_address):
        self.s_address = s_address

    def set_s_contact_details(self, s_contact_details):
        self.s_contact_details = s_contact_details

    def get_s_name(self):
        return self.s_name

    def get_s_ID(self):
        return self.s_ID

    def get_s_type(self):
        return self.s_type

    def get_s_address(self):
        return self.s_address

    def get_s_contact_details(self):
        return self.s_contact_details

class Catering_Company(Supplier):
    """Class to represent a catering company"""
    def __init__(self, s_name='', s_ID='', s_type=S_Type.C, s_address='', s_contact_details='', menu=[], c_min_guests=0, c_max_guests=0):
        super().__init__(s_name, s_ID, s_type, s_address, s_contact_details)
        self.menu = menu
        self.c_min_guests = c_min_guests
        self.c_max_guests = c_max_guests

    def set_menu(self, menu):
        self.menu = menu

    def set_c_min_guests(self, c_min_guests):
        self.c_min_guests = c_min_guests

    def set_c_max_guests(self, c_max_guests):
        self.c_max_guests = c_max_guests

    def get_menu(self):
        return self.menu

    def get_c_min_guests(self):
        return self.c_min_guests

    def get_c_max_guests(self):
        return self.c_max_guests

class Cleaning_Company(Supplier):
    def __init__(self, s_name='', s_ID='', s_type=S_Type.C, s_address='', s_contact_details=''):
        super().__init__(s_name, s_ID, s_type, s_address, s_contact_details)

class Decorations_Company(Supplier):
    def __init__(self, s_name='', s_ID='', s_type=S_Type.C, s_address='', s_contact_details=''):
        super().__init__(s_name, s_ID, s_type, s_address, s_contact_details)

class Entertainment_Company(Supplier):
    def __init__(self, s_name='', s_ID='', s_type=S_Type.C, s_address='', s_contact_details=''):
        super().__init__(s_name, s_ID, s_type, s_address, s_contact_details)

class Furniture_Company(Supplier):
    def __init__(self, s_name='', s_ID='', s_type=S_Type.C, s_address='', s_contact_details=''):
        super().__init__(s_name, s_ID, s_type, s_address, s_contact_details)

class SupplierManagementGUI:
    def __init__(self, master):
        self.master = master
        master.title("Supplier Management System")
        self.suppliers = []

        self.btn_add = tk.Button(master, text="Add Supplier", command=self.add_supplier)
        self.btn_add.pack()

        self.btn_delete = tk.Button(master, text="Delete Supplier", command=self.delete_supplier)
        self.btn_delete.pack()

        self.btn_modify = tk.Button(master, text="Modify Supplier", command=self.modify_supplier)
        self.btn_modify.pack()

        self.btn_display = tk.Button(master, text="Display Supplier", command=self.display_supplier)
        self.btn_display.pack()

    def add_supplier(self):
        def save_supplier():
            try:
                # Retrieve entered details
                s_name = entry_name.get().strip()
                s_ID = entry_id.get().strip()
                s_address = entry_address.get().strip()
                s_contact_details = entry_contact_details.get().strip()
                s_type = S_Type(entry_type_var.get())  # Convert the selected option to S_Type enum

                # Check if all details are provided
                if not (s_name and s_ID and s_address and s_contact_details):
                    raise ValueError("Please enter all details.")

                # Check if the ID already exists
                for supplier in self.suppliers:
                    if supplier.s_ID == s_ID:
                        raise ValueError("Supplier ID already exists.")

                # Check if name contains only letters and spaces
                if not s_name.replace(" ", "").isalpha():
                    raise ValueError("Name must contain only letters and spaces.")

                # Check if ID contains only numbers
                if not s_ID.isdigit():
                    raise ValueError("Supplier ID must contain only numbers.")

                # Check if address contains only letters and numbers
                if not s_address.replace(" ", "").isalnum():
                    raise ValueError("Address must contain only letters, numbers, and spaces.")

                # Check if contact details are a 9-digit number
                if not re.match(r"^\d{9}$", s_contact_details):
                    raise ValueError("Contact details must be a phone number with a length of 9 digits.")

                # Add supplier with input details
                new_supplier = Supplier(s_name, s_ID, s_type, s_address, s_contact_details)
                self.suppliers.append(new_supplier)

                # Close the add window
                add_window.destroy()
                messagebox.showinfo("Success", "Supplier added successfully.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        # Create a new window for adding supplier details
        add_window = tk.Toplevel(self.master)
        add_window.title("Add New Supplier")

        # Define labels and entry fields for supplier details
        lbl_name = tk.Label(add_window, text="Name:")
        lbl_name.grid(row=0, column=0, sticky="w")
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1)

        lbl_id = tk.Label(add_window, text="Supplier ID:")
        lbl_id.grid(row=1, column=0, sticky="w")
        entry_id = tk.Entry(add_window)
        entry_id.grid(row=1, column=1)

        lbl_address = tk.Label(add_window, text="Address:")
        lbl_address.grid(row=2, column=0, sticky="w")
        entry_address = tk.Entry(add_window)
        entry_address.grid(row=2, column=1)

        lbl_contact_details = tk.Label(add_window, text="Contact Details:")
        lbl_contact_details.grid(row=3, column=0, sticky="w")
        entry_contact_details = tk.Entry(add_window)
        entry_contact_details.grid(row=3, column=1)

        lbl_type = tk.Label(add_window, text="Type:")
        lbl_type.grid(row=4, column=0, sticky="w")
        types = [t.value for t in S_Type]
        entry_type_var = tk.StringVar(add_window)
        entry_type_var.set(types[0])  # Default value
        dropdown_type = tk.OptionMenu(add_window, entry_type_var, *types)
        dropdown_type.grid(row=4, column=1)

        # Button to save the supplier details
        btn_save = tk.Button(add_window, text="Save", command=save_supplier)
        btn_save.grid(row=5, column=0, columnspan=2)

    def delete_supplier(self):
        def delete():
            try:
                s_ID = entry_id.get().strip()
                for supplier in self.suppliers:
                    if supplier.s_ID == s_ID:
                        self.suppliers.remove(supplier)
                        messagebox.showinfo("Success", "Supplier deleted successfully.")
                        delete_window.destroy()
                        return
                messagebox.showerror("Error", "Supplier not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid supplier ID.")

        # Create a new window for deleting supplier
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Supplier")

        # Label and entry field for Supplier ID
        lbl_id = tk.Label(delete_window, text="Supplier ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(delete_window)
        entry_id.grid(row=0, column=1)

        # Button to delete supplier
        btn_delete = tk.Button(delete_window, text="Delete", command=delete)
        btn_delete.grid(row=1, column=0, columnspan=2)

    def modify_supplier(self):
        def modify_details(supplier, detail):
            def save_changes():
                try:
                    new_detail = entry_detail.get().strip()

                    if detail == "Name":
                        if not new_detail.replace(" ", "").isalpha():
                            raise ValueError("Name must contain only letters and spaces.")
                        supplier.s_name = new_detail
                    elif detail == "Address":
                        if not new_detail.replace(" ", "").isalnum():
                            raise ValueError("Address must contain only letters, numbers, and spaces.")
                        supplier.s_address = new_detail
                    elif detail == "Contact Details":
                        if not re.match(r"^\d{9}$", new_detail):
                            raise ValueError("Contact details must be a phone number with a length of 9 digits.")
                        supplier.s_contact_details = new_detail

                    messagebox.showinfo("Success", f"Supplier {detail} modified successfully.")
                    modify_window.destroy()
                except ValueError as e:
                    messagebox.showerror("Error", str(e))

            # Create a new window for modifying the selected detail
            modify_window = tk.Toplevel()
            modify_window.title(f"Modify {detail}")

            # Label and entry field for the selected detail
            lbl_detail = tk.Label(modify_window, text=f"{detail}:")
            lbl_detail.grid(row=0, column=0, sticky="w")
            entry_detail = tk.Entry(modify_window)
            entry_detail.grid(row=0, column=1)

            # Set default value in entry field based on the selected detail
            if detail == "Name":
                entry_detail.insert(0, supplier.s_name)
            elif detail == "Address":
                entry_detail.insert(0, supplier.s_address)
            elif detail == "Contact Details":
                entry_detail.insert(0, supplier.s_contact_details)

            # Button to save the changes
            btn_save = tk.Button(modify_window, text="Save Changes", command=save_changes)
            btn_save.grid(row=1, column=0, columnspan=2)

        def verify_id():
            try:
                s_ID = entry_id.get()
                for supplier in self.suppliers:
                    if supplier.s_ID == s_ID:
                        modify_window = tk.Toplevel()
                        modify_window.title("Modify Supplier Details")

                        # Create a menu with different options for modifying supplier details
                        options = ["Name", "Address", "Contact Details"]
                        for i, option in enumerate(options):
                            btn_option = tk.Button(modify_window, text=option,
                                                   command=lambda o=option: modify_details(supplier, o))
                            btn_option.grid(row=i, column=0, columnspan=2)

                        return
                messagebox.showerror("Error", "Supplier not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid supplier ID.")

        # Create a new window for verifying Supplier ID
        verify_window = tk.Toplevel(self.master)
        verify_window.title("Verify Supplier ID")

        # Label and entry field for Supplier ID
        lbl_id = tk.Label(verify_window, text="Supplier ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(verify_window)
        entry_id.grid(row=0, column=1)

        # Button to verify Supplier ID
        btn_verify = tk.Button(verify_window, text="Verify", command=verify_id)
        btn_verify.grid(row=1, column=0, columnspan=2)

    def display_supplier(self):
        def display():
            try:
                s_ID = entry_id.get().strip()
                for supplier in self.suppliers:
                    if supplier.s_ID == s_ID:
                        details = f"Name: {supplier.s_name}\nID: {supplier.s_ID}\nType: {supplier.s_type.value}\n" \
                                  f"Address: {supplier.s_address}\nContact Details: {supplier.s_contact_details}"
                        messagebox.showinfo("Supplier Details", details)
                        return
                messagebox.showerror("Error", "Supplier not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid supplier ID.")

        # Create a new window for displaying supplier details
        display_window = tk.Toplevel(self.master)
        display_window.title("Display Supplier Details")

        # Label and entry field for Supplier ID
        lbl_id = tk.Label(display_window, text="Supplier ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(display_window)
        entry_id.grid(row=0, column=1)

        # Button to display supplier details
        btn_display = tk.Button(display_window, text="Display", command=display)
        btn_display.grid(row=1, column=0, columnspan=2)


def main():
    root = tk.Tk()
    app = SupplierManagementGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()