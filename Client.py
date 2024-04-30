import tkinter as tk
from tkinter import messagebox
import re

class Client:
    """Class to represent a client"""
    def __init__(self, clt_name='', clt_ID='', clt_address='', clt_contact_details='', budget=0.0):
        self.clt_name = clt_name
        self.clt_ID = clt_ID
        self.clt_address = clt_address
        self.clt_contact_details = clt_contact_details
        self.budget = budget

    def set_clt_name(self, clt_name):
        self.clt_name = clt_name

    def set_clt_ID(self, clt_ID):
        self.clt_ID = clt_ID

    def set_clt_address(self, clt_address):
        self.clt_address = clt_address

    def set_clt_contact_details(self, clt_contact_details):
        self.clt_contact_details = clt_contact_details

    def set_budget(self, budget):
        self.budget = budget

    def get_clt_name(self):
        return self.clt_name

    def get_clt_ID(self):
        return self.clt_ID

    def get_clt_address(self):
        return self.clt_address

    def get_clt_contact_details(self):
        return self.clt_contact_details

    def get_budget(self):
        return self.budget

    def add_client(self, clients, clt_name, clt_ID, clt_address, clt_contact_details, budget):
        # Validation
        if not (clt_name.strip().replace(" ", "").isalpha()):
            raise ValueError("Name must contain only letters and spaces.")
        if not (clt_ID.isdigit()):
            raise ValueError("Client ID must contain only numbers.")
        if not (clt_address.strip().replace(" ", "").isalnum()):
            raise ValueError("Address must contain only letters, numbers, and spaces.")
        if not re.match(r"^\d{9}$", clt_contact_details):
            raise ValueError("Contact details must be a phone number with a length of 9 digits.")
        if not (budget.replace('.', '', 1).isdigit()):  # Check if it's a valid floating-point number
            raise ValueError("Budget must be a valid number.")

        new_client = Client(clt_name, clt_ID, clt_address, clt_contact_details, float(budget))
        clients.append(new_client)
        return new_client

    def delete_client(self, clients, clt_ID):
        for client in clients:
            if client.clt_ID == clt_ID:
                clients.remove(client)
                return True
        return False

    def modify_client(self, clients, clt_ID, clt_name=None, clt_address=None, clt_contact_details=None, budget=None):
        for client in clients:
            if client.clt_ID == clt_ID:
                if clt_name is not None:
                    client.clt_name = clt_name
                if clt_address is not None:
                    client.clt_address = clt_address
                if clt_contact_details is not None:
                    client.clt_contact_details = clt_contact_details
                if budget is not None:
                    client.budget = float(budget)
                return True
        return False

    def display_client(self, clients, clt_ID):
        for client in clients:
            if client.clt_ID == clt_ID:
                return client
        return None

class ClientManagementGUI:
    def __init__(self, master):
        self.master = master
        master.title("Client Management System")
        self.clients = []

        self.btn_add = tk.Button(master, text="Add Client", command=self.add_client)
        self.btn_add.pack()

        self.btn_delete = tk.Button(master, text="Delete Client", command=self.delete_client)
        self.btn_delete.pack()

        self.btn_modify = tk.Button(master, text="Modify Client", command=self.modify_client)
        self.btn_modify.pack()

        self.btn_display = tk.Button(master, text="Display Client", command=self.display_client)
        self.btn_display.pack()

    def add_client(self):
        def save_client():
            try:
                # Retrieve entered details
                clt_name = entry_name.get()
                clt_ID = entry_id.get()
                clt_address = entry_address.get()
                clt_contact_details = entry_contact_details.get()
                budget = entry_budget.get()

                # Add client with input details
                new_client = Client().add_client(self.clients, clt_name, clt_ID, clt_address, clt_contact_details, budget)

                # Close the add window
                add_window.destroy()
                messagebox.showinfo("Success", "Client added successfully.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        # Create a new window for adding client details
        add_window = tk.Toplevel(self.master)
        add_window.title("Add New Client")

        # Define labels and entry fields for client details
        lbl_name = tk.Label(add_window, text="Name:")
        lbl_name.grid(row=0, column=0, sticky="w")
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1)

        lbl_id = tk.Label(add_window, text="Client ID:")
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

        lbl_budget = tk.Label(add_window, text="Budget:")
        lbl_budget.grid(row=4, column=0, sticky="w")
        entry_budget = tk.Entry(add_window)
        entry_budget.grid(row=4, column=1)

        # Button to save the client details
        btn_save = tk.Button(add_window, text="Save", command=save_client)
        btn_save.grid(row=5, column=0, columnspan=2)

    def delete_client(self):
        def delete():
            try:
                clt_ID = entry_id.get().strip()
                if Client().delete_client(self.clients, clt_ID):
                    messagebox.showinfo("Success", "Client deleted successfully.")
                else:
                    messagebox.showerror("Error", "Client not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid client ID.")

        # Create a new window for deleting client
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Client")

        # Label and entry field for Client ID
        lbl_id = tk.Label(delete_window, text="Client ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(delete_window)
        entry_id.grid(row=0, column=1)

        # Button to delete client
        btn_delete = tk.Button(delete_window, text="Delete", command=delete)
        btn_delete.grid(row=1, column=0, columnspan=2)

    def modify_client(self):
        def modify():
            try:
                clt_ID = entry_id.get().strip()
                clt_name = entry_name.get().strip()
                clt_address = entry_address.get().strip()
                clt_contact_details = entry_contact_details.get().strip()
                budget = entry_budget.get().strip()

                if Client().modify_client(self.clients, clt_ID, clt_name, clt_address, clt_contact_details, budget):
                    messagebox.showinfo("Success", "Client details modified successfully.")
                else:
                    messagebox.showerror("Error", "Client not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid budget.")

        # Create a new window for modifying client details
        modify_window = tk.Toplevel(self.master)
        modify_window.title("Modify Client")

        # Label and entry field for Client ID
        lbl_id = tk.Label(modify_window, text="Client ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(modify_window)
        entry_id.grid(row=0, column=1)

        lbl_name = tk.Label(modify_window, text="New Name:")
        lbl_name.grid(row=1, column=0, sticky="w")
        entry_name = tk.Entry(modify_window)
        entry_name.grid(row=1, column=1)

        lbl_address = tk.Label(modify_window, text="New Address:")
        lbl_address.grid(row=2, column=0, sticky="w")
        entry_address = tk.Entry(modify_window)
        entry_address.grid(row=2, column=1)

        lbl_contact_details = tk.Label(modify_window, text="New Contact Details:")
        lbl_contact_details.grid(row=3, column=0, sticky="w")
        entry_contact_details = tk.Entry(modify_window)
        entry_contact_details.grid(row=3, column=1)

        lbl_budget = tk.Label(modify_window, text="New Budget:")
        lbl_budget.grid(row=4, column=0, sticky="w")
        entry_budget = tk.Entry(modify_window)
        entry_budget.grid(row=4, column=1)

        # Button to modify client details
        btn_modify = tk.Button(modify_window, text="Modify", command=modify)
        btn_modify.grid(row=5, column=0, columnspan=2)

    def display_client(self):
        def display():
            try:
                clt_ID = entry_id.get().strip()
                client = Client().display_client(self.clients, clt_ID)
                if client:
                    details = f"Name: {client.clt_name}\nID: {client.clt_ID}\nAddress: {client.clt_address}\n" \
                              f"Contact Details: {client.clt_contact_details}\nBudget: {client.budget}"
                    messagebox.showinfo("Client Details", details)
                else:
                    messagebox.showerror("Error", "Client not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid client ID.")

        # Create a new window for displaying client details
        display_window = tk.Toplevel(self.master)
        display_window.title("Display Client Details")

        # Label and entry field for Client ID
        lbl_id = tk.Label(display_window, text="Client ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(display_window)
        entry_id.grid(row=0, column=1)

        # Button to display client details
        btn_display = tk.Button(display_window, text="Display", command=display)
        btn_display.grid(row=1, column=0, columnspan=2)


def main():
    root = tk.Tk()
    app = ClientManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

