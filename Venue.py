import tkinter as tk
from tkinter import messagebox
import re


class Venue:
    """Class to represent a venue"""

    def __init__(self, v_name='', v_ID='', v_address='', v_contact='', v_min_guests=0, v_max_guests=0):
        self.v_name = v_name
        self.v_ID = v_ID
        self.v_address = v_address
        self.v_contact = v_contact
        self.v_min_guests = v_min_guests
        self.v_max_guests = v_max_guests

    def set_v_name(self, v_name):
        self.v_name = v_name

    def set_v_ID(self, v_ID):
        self.v_ID = v_ID

    def set_v_address(self, v_address):
        self.v_address = v_address

    def set_v_contact(self, v_contact):
        self.v_contact = v_contact

    def set_v_min_guests(self, v_min_guests):
        self.v_min_guests = v_min_guests

    def set_v_max_guests(self, v_max_guests):
        self.v_max_guests = v_max_guests

    def get_v_name(self):
        return self.v_name

    def get_v_ID(self):
        return self.v_ID

    def get_v_address(self):
        return self.v_address

    def get_v_contact(self):
        return self.v_contact

    def get_v_min_guests(self):
        return self.v_min_guests

    def get_v_max_guests(self):
        return self.v_max_guests

    def add_venue(self, venues, v_name, v_ID, v_address, v_contact, v_min_guests, v_max_guests):
        # Validation
        if not (v_name.strip().replace(" ", "").isalpha()):
            raise ValueError("Name must contain only letters and spaces.")
        if not (v_ID.isdigit()):
            raise ValueError("Venue ID must contain only numbers.")
        if not (v_address.strip().replace(" ", "").isalnum()):
            raise ValueError("Address must contain only letters, numbers, and spaces.")
        if not re.match(r"^\d{9}$", v_contact):
            raise ValueError("Contact must be a phone number with a length of 9 digits.")
        if not (v_min_guests.isdigit() and v_max_guests.isdigit()):
            raise ValueError("Minimum and maximum guests must contain only numbers.")
        if int(v_min_guests) >= int(v_max_guests):
            raise ValueError("Maximum guests must be greater than minimum guests.")

        new_venue = Venue(v_name, v_ID, v_address, v_contact, int(v_min_guests), int(v_max_guests))
        venues.append(new_venue)
        return new_venue

    def delete_venue(self, venues, v_ID):
        for venue in venues:
            if venue.v_ID == v_ID:
                venues.remove(venue)
                return True
        return False

    def modify_venue(self, venues, v_ID, v_name=None, v_address=None, v_contact=None, v_min_guests=None,
                     v_max_guests=None):
        for venue in venues:
            if venue.v_ID == v_ID:
                if v_name is not None:
                    venue.v_name = v_name
                if v_address is not None:
                    venue.v_address = v_address
                if v_contact is not None:
                    venue.v_contact = v_contact
                if v_min_guests is not None:
                    venue.v_min_guests = int(v_min_guests)
                if v_max_guests is not None:
                    venue.v_max_guests = int(v_max_guests)
                return True
        return False

    def display_venue(self, venues, v_ID):
        for venue in venues:
            if venue.v_ID == v_ID:
                return venue
        return None


class VenueManagementGUI:
    def __init__(self, master):
        self.master = master
        master.title("Venue Management System")
        self.venues = []

        self.btn_add = tk.Button(master, text="Add Venue", command=self.add_venue)
        self.btn_add.pack()

        self.btn_delete = tk.Button(master, text="Delete Venue", command=self.delete_venue)
        self.btn_delete.pack()

        self.btn_modify = tk.Button(master, text="Modify Venue", command=self.modify_venue)
        self.btn_modify.pack()

        self.btn_display = tk.Button(master, text="Display Venue", command=self.display_venue)
        self.btn_display.pack()

    def add_venue(self):
        def save_venue():
            try:
                # Retrieve entered details
                v_name = entry_name.get()
                v_ID = entry_id.get()
                v_address = entry_address.get()
                v_contact = entry_contact.get()
                v_min_guests = entry_min_guests.get()
                v_max_guests = entry_max_guests.get()

                # Add venue with input details
                new_venue = Venue().add_venue(self.venues, v_name, v_ID, v_address, v_contact, v_min_guests,
                                              v_max_guests)

                # Close the add window
                add_window.destroy()
                messagebox.showinfo("Success", "Venue added successfully.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        # Create a new window for adding venue details
        add_window = tk.Toplevel(self.master)
        add_window.title("Add New Venue")

        # Define labels and entry fields for venue details
        lbl_name = tk.Label(add_window, text="Name:")
        lbl_name.grid(row=0, column=0, sticky="w")
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1)

        lbl_id = tk.Label(add_window, text="Venue ID:")
        lbl_id.grid(row=1, column=0, sticky="w")
        entry_id = tk.Entry(add_window)
        entry_id.grid(row=1, column=1)

        lbl_address = tk.Label(add_window, text="Address:")
        lbl_address.grid(row=2, column=0, sticky="w")
        entry_address = tk.Entry(add_window)
        entry_address.grid(row=2, column=1)

        lbl_contact = tk.Label(add_window, text="Contact:")
        lbl_contact.grid(row=3, column=0, sticky="w")
        entry_contact = tk.Entry(add_window)
        entry_contact.grid(row=3, column=1)

        lbl_min_guests = tk.Label(add_window, text="Min Guests:")
        lbl_min_guests.grid(row=4, column=0, sticky="w")
        entry_min_guests = tk.Entry(add_window)
        entry_min_guests.grid(row=4, column=1)

        lbl_max_guests = tk.Label(add_window, text="Max Guests:")
        lbl_max_guests.grid(row=5, column=0, sticky="w")
        entry_max_guests = tk.Entry(add_window)
        entry_max_guests.grid(row=5, column=1)

        # Button to save the venue details
        btn_save = tk.Button(add_window, text="Save", command=save_venue)
        btn_save.grid(row=6, column=0, columnspan=2)

    def delete_venue(self):
        def delete():
            try:
                v_ID = entry_id.get().strip()
                if Venue().delete_venue(self.venues, v_ID):
                    messagebox.showinfo("Success", "Venue deleted successfully.")
                else:
                    messagebox.showerror("Error", "Venue not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid venue ID.")

        # Create a new window for deleting venue
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Venue")

        # Label and entry field for Venue ID
        lbl_id = tk.Label(delete_window, text="Venue ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(delete_window)
        entry_id.grid(row=0, column=1)

        # Button to delete venue
        btn_delete = tk.Button(delete_window, text="Delete", command=delete)
        btn_delete.grid(row=1, column=0, columnspan=2)

    def modify_venue(self):
        modify_window = None  # Define modify_window as a global variable

        def modify_details(venue, detail):
            def save_changes():
                try:
                    new_detail = entry_detail.get().strip()

                    if detail == "Name":
                        if not (new_detail.replace(" ", "").isalpha()):
                            raise ValueError("Name must contain only letters and spaces.")
                        venue.v_name = new_detail
                    elif detail == "Address":
                        if not (new_detail.replace(" ", "").isalnum()):
                            raise ValueError("Address must contain only letters, numbers, and spaces.")
                        venue.v_address = new_detail
                    elif detail == "Contact":
                        if not re.match(r"^\d{9}$", new_detail):
                            raise ValueError("Contact must be a phone number with a length of 9 digits.")
                        venue.v_contact = new_detail
                    elif detail == "Min Guests":
                        if not (new_detail.isdigit()):
                            raise ValueError("Minimum guests must contain only numbers.")
                        venue.v_min_guests = int(new_detail)
                    elif detail == "Max Guests":
                        if not (new_detail.isdigit()):
                            raise ValueError("Maximum guests must contain only numbers.")
                        if int(new_detail) <= venue.v_min_guests:
                            raise ValueError("Maximum guests must be greater than minimum guests.")
                        venue.v_max_guests = int(new_detail)

                    messagebox.showinfo("Success", f"Venue {detail} modified successfully.")
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
                entry_detail.insert(0, venue.v_name)
            elif detail == "Address":
                entry_detail.insert(0, venue.v_address)
            elif detail == "Contact":
                entry_detail.insert(0, venue.v_contact)
            elif detail == "Min Guests":
                entry_detail.insert(0, venue.v_min_guests)
            elif detail == "Max Guests":
                entry_detail.insert(0, venue.v_max_guests)

            # Button to save the changes
            btn_save = tk.Button(modify_window, text="Save Changes", command=save_changes)
            btn_save.grid(row=1, column=0, columnspan=2)

        def verify_id():
            try:
                # Function to verify Venue ID
                v_ID = entry_id.get()
                for venue in self.venues:
                    if venue.v_ID == v_ID:
                        # If ID is correct, show the modify menu
                        nonlocal modify_window
                        modify_window = tk.Toplevel()
                        modify_window.title("Modify Venue Details")

                        # Create a menu with different options for modifying venue details
                        options = ["Name", "Address", "Contact", "Min Guests", "Max Guests"]
                        for i, option in enumerate(options):
                            btn_option = tk.Button(modify_window, text=option,
                                                   command=lambda o=option: modify_details(venue, o))
                            btn_option.grid(row=i, column=0, columnspan=2)

                        return
                messagebox.showerror("Error", "Venue not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid venue ID.")

        # Create a new window for verifying Venue ID
        verify_window = tk.Toplevel(self.master)
        verify_window.title("Verify Venue ID")

        # Label and entry field for Venue ID
        lbl_id = tk.Label(verify_window, text="Venue ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(verify_window)
        entry_id.grid(row=0, column=1)

        # Button to verify Venue ID
        btn_verify = tk.Button(verify_window, text="Verify", command=verify_id)
        btn_verify.grid(row=1, column=0, columnspan=2)

    def display_venue(self):
        def display():
            try:
                v_ID = entry_id.get().strip()
                venue = Venue().display_venue(self.venues, v_ID)
                if venue:
                    details = f"Name: {venue.v_name}\nID: {venue.v_ID}\nAddress: {venue.v_address}\n" \
                              f"Contact: {venue.v_contact}\nMin Guests: {venue.v_min_guests}\nMax Guests: {venue.v_max_guests}"
                    messagebox.showinfo("Venue Details", details)
                else:
                    messagebox.showerror("Error", "Venue not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid venue ID.")

        # Create a new window for displaying venue details
        display_window = tk.Toplevel(self.master)
        display_window.title("Display Venue Details")

        # Label and entry field for Venue ID
        lbl_id = tk.Label(display_window, text="Venue ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(display_window)
        entry_id.grid(row=0, column=1)

        # Button to display venue details
        btn_display = tk.Button(display_window, text="Display", command=display)
        btn_display.grid(row=1, column=0, columnspan=2)


def main():
    root = tk.Tk()
    app = VenueManagementGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
