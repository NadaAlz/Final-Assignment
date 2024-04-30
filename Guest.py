import tkinter as tk
from tkinter import messagebox
import re

class Guest:
    """Class to represent a guest"""
    def __init__(self, gst_name='', gst_ID='', gst_address='', gst_contact_details=''):
        self.gst_name = gst_name
        self.gst_ID = gst_ID
        self.gst_address = gst_address
        self.gst_contact_details = gst_contact_details

    def set_gst_name(self, gst_name):
        self.gst_name = gst_name

    def set_gst_ID(self, gst_ID):
        self.gst_ID = gst_ID

    def set_gst_address(self, gst_address):
        self.gst_address = gst_address

    def set_gst_contact_details(self, gst_contact_details):
        self.gst_contact_details = gst_contact_details

    def get_gst_name(self):
        return self.gst_name

    def get_gst_ID(self):
        return self.gst_ID

    def get_gst_address(self):
        return self.gst_address

    def get_gst_contact_details(self):
        return self.gst_contact_details

    def add_guest(self, guests, gst_name, gst_ID, gst_address, gst_contact_details):
        # Validation
        if not (gst_name.strip().replace(" ", "").isalpha()):
            raise ValueError("Name must contain only letters and spaces.")
        if not (gst_ID.isdigit()):
            raise ValueError("Guest ID must contain only numbers.")
        if not (gst_address.strip().replace(" ", "").isalnum()):
            raise ValueError("Address must contain only letters, numbers, and spaces.")
        if not re.match(r"^\d{9}$", gst_contact_details):
            raise ValueError("Contact details must be a phone number with a length of 9 digits.")

        # Check if the ID already exists
        for guest in guests:
            if guest.gst_ID == gst_ID:
                raise ValueError("Guest with the same ID already exists.")

        new_guest = Guest(gst_name, gst_ID, gst_address, gst_contact_details)
        guests.append(new_guest)
        return new_guest

    def delete_guest(self, guests, gst_ID):
        for guest in guests:
            if guest.gst_ID == gst_ID:
                guests.remove(guest)
                return True
        return False

    def modify_guest(self, guests, gst_ID, gst_name=None, gst_address=None, gst_contact_details=None):
        for guest in guests:
            if guest.gst_ID == gst_ID:
                if gst_name is not None:
                    guest.gst_name = gst_name
                if gst_address is not None:
                    guest.gst_address = gst_address
                if gst_contact_details is not None:
                    guest.gst_contact_details = gst_contact_details
                return True
        return False

    def display_guest(self, guests, gst_ID):
        for guest in guests:
            if guest.gst_ID == gst_ID:
                return guest
        return None


class GuestManagementGUI:
    def __init__(self, master):
        self.master = master
        master.title("Guest Management System")
        self.guest_management = Guest()

        self.guests = []

        self.btn_add = tk.Button(master, text="Add Guest", command=self.add_guest)
        self.btn_add.pack()

        self.btn_delete = tk.Button(master, text="Delete Guest", command=self.delete_guest)
        self.btn_delete.pack()

        self.btn_modify = tk.Button(master, text="Modify Guest", command=self.modify_guest)
        self.btn_modify.pack()

        self.btn_display = tk.Button(master, text="Display Guest", command=self.display_guest)
        self.btn_display.pack()

    def add_guest(self):
        def save_guest():
            try:
                gst_name = entry_name.get()
                gst_ID = entry_id.get()
                gst_address = entry_address.get()
                gst_contact_details = entry_contact_details.get()

                new_guest = self.guest_management.add_guest(self.guests, gst_name, gst_ID, gst_address, gst_contact_details)

                add_window.destroy()
                messagebox.showinfo("Success", "Guest added successfully.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        add_window = tk.Toplevel(self.master)
        add_window.title("Add New Guest")

        lbl_name = tk.Label(add_window, text="Name:")
        lbl_name.grid(row=0, column=0, sticky="w")
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1)

        lbl_id = tk.Label(add_window, text="Guest ID:")
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

        btn_save = tk.Button(add_window, text="Save", command=save_guest)
        btn_save.grid(row=4, column=0, columnspan=2)

    def delete_guest(self):
        def delete():
            try:
                gst_ID = entry_id.get().strip()
                if self.guest_management.delete_guest(self.guests, gst_ID):
                    messagebox.showinfo("Success", "Guest deleted successfully.")
                else:
                    messagebox.showerror("Error", "Guest not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid guest ID.")

        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Guest")

        lbl_id = tk.Label(delete_window, text="Guest ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(delete_window)
        entry_id.grid(row=0, column=1)

        btn_delete = tk.Button(delete_window, text="Delete", command=delete)
        btn_delete.grid(row=1, column=0, columnspan=2)

    def modify_guest(self):
        modify_window = None  # Define modify_window as a global variable

        def modify_details(guest, detail):
            def save_changes():
                try:
                    new_detail = entry_detail.get().strip()

                    if detail == "Name":
                        if not (new_detail.replace(" ", "").isalpha()):
                            raise ValueError("Name must contain only letters and spaces.")
                        guest.gst_name = new_detail
                    elif detail == "Address":
                        if not (new_detail.replace(" ", "").isalnum()):
                            raise ValueError("Address must contain only letters, numbers, and spaces.")
                        guest.gst_address = new_detail
                    elif detail == "Contact Details":
                        if not re.match(r"^\d{9}$", new_detail):
                            raise ValueError("Contact details must be a phone number with a length of 9 digits.")
                        guest.gst_contact_details = new_detail

                    messagebox.showinfo("Success", f"Guest {detail} modified successfully.")
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
                entry_detail.insert(0, guest.gst_name)
            elif detail == "Address":
                entry_detail.insert(0, guest.gst_address)
            elif detail == "Contact Details":
                entry_detail.insert(0, guest.gst_contact_details)

            # Button to save the changes
            btn_save = tk.Button(modify_window, text="Save Changes", command=save_changes)
            btn_save.grid(row=1, column=0, columnspan=2)

        def verify_id():
            try:
                # Function to verify Guest ID
                gst_ID = entry_id.get()
                for guest in self.guests:
                    if guest.gst_ID == gst_ID:
                        # If ID is correct, show the modify menu
                        nonlocal modify_window
                        modify_window = tk.Toplevel()
                        modify_window.title("Modify Guest Details")

                        # Create a menu with different options for modifying guest details
                        options = ["Name", "Address", "Contact Details"]
                        for i, option in enumerate(options):
                            btn_option = tk.Button(modify_window, text=option,
                                                   command=lambda o=option: modify_details(guest, o))
                            btn_option.grid(row=i, column=0, columnspan=2)

                        return
                messagebox.showerror("Error", "Guest not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid guest ID.")

        # Create a new window for verifying Guest ID
        verify_window = tk.Toplevel(self.master)
        verify_window.title("Verify Guest ID")

        # Label and entry field for Guest ID
        lbl_id = tk.Label(verify_window, text="Guest ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(verify_window)
        entry_id.grid(row=0, column=1)

        # Button to verify Guest ID
        btn_verify = tk.Button(verify_window, text="Verify", command=verify_id)
        btn_verify.grid(row=1, column=0, columnspan=2)

    def display_guest(self):
        def display():
            try:
                gst_ID = entry_id.get().strip()
                guest = self.guest_management.display_guest(self.guests, gst_ID)
                if guest:
                    details = f"Name: {guest.gst_name}\nID: {guest.gst_ID}\nAddress: {guest.gst_address}\n" \
                              f"Contact Details: {guest.gst_contact_details}"
                    messagebox.showinfo("Guest Details", details)
                else:
                    messagebox.showerror("Error", "Guest not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid guest ID.")

        display_window = tk.Toplevel(self.master)
        display_window.title("Display Guest Details")

        lbl_id = tk.Label(display_window, text="Guest ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(display_window)
        entry_id.grid(row=0, column=1)

        btn_display = tk.Button(display_window, text="Display", command=display)
        btn_display.grid(row=1, column=0, columnspan=2)


def main():
    root = tk.Tk()
    app = GuestManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

