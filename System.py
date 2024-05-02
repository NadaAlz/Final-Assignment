from Employee import Manager
from Employee import Employee
from Employee import Job_Title
from Client import Client
from Guest import Guest
from Venue import Venue
from Supplier import Supplier
from Supplier import S_Type
from Event import Event
from Event import Theme

import tkinter as tk
from tkinter import messagebox, OptionMenu, Toplevel, Label, Entry, Button
from tkinter import ttk
import re


import pickle



class IntegratedSystemGUI:
    def __init__(self, master):
        self.master = master
        self.clients = []
        self.guest_management = Guest()
        self.guests = []
        self.venues = []
        self.suppliers = []
        self.supplier = Supplier()
        self.events = []
        self.employees = []
        self.save_data()
        self.load_data()  # Load data when the application starts
        master.title("The Best Events Company System")

        # Create buttons for each entity
        self.btn_employee = tk.Button(master, text="Employee", command=self.manage_employees)
        self.btn_employee.pack()

        self.btn_client = tk.Button(master, text="Client", command=self.manage_clients)
        self.btn_client.pack()

        self.btn_venue = tk.Button(master, text="Venue", command=self.manage_venues)
        self.btn_venue.pack()

        self.btn_supplier = tk.Button(master, text="Supplier", command=self.manage_suppliers)
        self.btn_supplier.pack()

        self.btn_guest = tk.Button(master, text="Guest", command=self.manage_guests)
        self.btn_guest.pack()

        self.btn_event = tk.Button(master, text="Event", command=self.manage_events)
        self.btn_event.pack()

    def save_data(self):
        self.save_events()
        self.save_venues()
        self.save_guests()
        self.save_clients()
        self.save_suppliers()
        self.save_employees()

    def load_data(self):
        self.load_events()
        self.load_venues()
        self.load_guests()
        self.load_clients()
        self.load_suppliers()
        self.load_employees()

    def save_events(self):
        with open('events.bin', 'wb') as f:
            pickle.dump(self.events, f)

    def load_events(self):
        try:
            with open('events.bin', 'rb') as f:
                self.events = pickle.load(f)
        except FileNotFoundError:
            self.events = []

    def save_venues(self):
        with open('venues.bin', 'wb') as f:
            pickle.dump(self.venues, f)

    def load_venues(self):
        try:
            with open('venues.bin', 'rb') as f:
                self.venues = pickle.load(f)
        except FileNotFoundError:
            self.venues = []

    def save_guests(self):
        with open('guests.bin', 'wb') as f:
            pickle.dump(self.guests, f)

    def load_guests(self):
        try:
            with open('guests.bin', 'rb') as f:
                self.guests = pickle.load(f)
        except FileNotFoundError:
            self.guests = []

    def save_clients(self):
        with open('clients.bin', 'wb') as f:
            pickle.dump(self.clients, f)

    def load_clients(self):
        try:
            with open('clients.bin', 'rb') as f:
                self.clients = pickle.load(f)
        except FileNotFoundError:
            self.clients = []

    def save_suppliers(self):
        with open('suppliers.bin', 'wb') as f:
            pickle.dump(self.suppliers, f)

    def load_suppliers(self):
        try:
            with open('suppliers.bin', 'rb') as f:
                self.suppliers = pickle.load(f)
        except FileNotFoundError:
            self.suppliers = []

    def save_employees(self):
        with open('employees.bin', 'wb') as f:
            pickle.dump(self.employees, f)

    def load_employees(self):
        try:
            with open('employees.bin', 'rb') as f:
                self.employees = pickle.load(f)
        except FileNotFoundError:
            self.employees = []

    def manage_events(self):


        def add_event():
            def save_event():
                try:

                    # Retrieve entered details
                    e_ID = entry_e_id.get()
                    theme = theme_var.get()
                    date = entry_date.get()
                    time = entry_time.get()
                    duration = entry_duration.get()
                    v_address = venue_var.get()
                    clt_ID = client_var.get()
                    catering = catering_var.get()  # Get selected catering option
                    cleaning = cleaning_var.get()  # Get selected cleaning option
                    decoration = decoration_var.get()  # Get selected decoration option
                    entertainment = entertainment_var.get()  # Get selected entertainment option
                    furniture = furniture_var.get()  # Get selected furniture option
                    gst_ID = entry_gst_ID.get()

                    if '' in [e_ID, theme, date, time, duration, v_address, clt_ID, catering,
                              cleaning, decoration, entertainment, furniture]:
                        raise ValueError("Please enter all details.")

                        # Validate input formats
                    if not re.match(r"^\d{1,2}-\d{1,2}-\d{4}$", date):
                        raise ValueError("Date must be in the form of DD-MM-YYYY.")
                    if not re.match(r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$", time):
                        raise ValueError("Time must be in the form of HH:MM.")
                    if not duration.isdigit() or not (1 <= int(duration) <= 10):
                        raise ValueError("Duration must be a number between 1 and 10.")

                    if not re.match(r"^\d+(,\d+)*$", gst_ID):
                        raise ValueError("Guest IDs must be numbers separated by commas.")

                    gst_ID = gst_ID.split(',')  # Convert string to list of guest IDs

                    for event in self.events:
                        if event.e_ID == e_ID:
                            raise ValueError(f"Event with ID {e_ID} already exists.")





                    # Add event with input details
                    new_event = Event(e_ID, theme, date,time, duration, v_address, clt_ID, catering, cleaning, decoration, entertainment, furniture, gst_ID)

                    self.events.append(new_event)

                    # Close the add window
                    add_window.destroy()
                    messagebox.showinfo("Success", "Event added successfully.")
                except ValueError as e:
                    messagebox.showerror("Error", str(e))

            # Create a new window for adding event details
            add_window = Toplevel(self.master)
            add_window.title("Add New Event")

            # Define labels and entry fields for event details
            lbl_e_id = Label(add_window, text="Event ID:")
            lbl_e_id.grid(row=0, column=0, sticky="w")
            entry_e_id = Entry(add_window)
            entry_e_id.grid(row=0, column=1)

            lbl_theme = Label(add_window, text="Theme:")
            lbl_theme.grid(row=1, column=0, sticky="w")
            theme = [theme.value for theme in Theme]
            theme_var = tk.StringVar(add_window)
            theme_var.set(theme[0])  # Default value
            theme_dropdown = OptionMenu(add_window, theme_var, *theme)
            theme_dropdown.grid(row=1, column=1)

            lbl_date = Label(add_window, text="Date:")
            lbl_date.grid(row=2, column=0, sticky="w")
            entry_date = Entry(add_window)
            entry_date.grid(row=2, column=1)

            lbl_time = Label(add_window, text="Time:")
            lbl_time.grid(row=3, column=0, sticky="w")
            entry_time = Entry(add_window)
            entry_time.grid(row=3, column=1)

            lbl_duration = Label(add_window, text="Duration:")
            lbl_duration.grid(row=4, column=0, sticky="w")
            entry_duration = Entry(add_window)
            entry_duration.grid(row=4, column=1)

            lbl_v_address = Label(add_window, text="Venue Address:")
            lbl_v_address.grid(row=5, column=0, sticky="w")
            venue_var = tk.StringVar(add_window)
            venue_var.set("")
            venues_array = [venue.v_address for venue in self.venues]
            venue_dropdown = OptionMenu(add_window, venue_var, *venues_array)
            venue_dropdown.grid(row=5, column=1)

            lbl_clt_ID = Label(add_window, text="Client ID:")
            lbl_clt_ID.grid(row=6, column=0, sticky="w")
            client_var = tk.StringVar(add_window)
            client_var.set("")  # Default value
            # Extract clt_ID from each client and store in a list
            clients_array = [client.clt_ID for client in self.clients]
            # Create the dropdown menu with the list of clt_IDs
            client_dropdown = OptionMenu(add_window, client_var, *clients_array)
            client_dropdown.grid(row=6, column=1)

            # Create menus for selecting from available options
            lbl_catering = Label(add_window, text="Catering:")
            lbl_catering.grid(row=7, column=0, sticky="w")
            catering_var = tk.StringVar(add_window)
            catering_var.set("")  # Default value
            catering_array = [supplier.s_name for supplier in self.suppliers if supplier.s_type == S_Type.C]
            catering_dropdown = OptionMenu(add_window, catering_var, *catering_array)
            catering_dropdown.grid(row=7, column=1)

            lbl_cleaning = Label(add_window, text="Cleaning:")
            lbl_cleaning.grid(row=8, column=0, sticky="w")
            cleaning_var = tk.StringVar(add_window)
            cleaning_var.set("")  # Default value
            cleaning_array = [supplier.s_name for supplier in self.suppliers if supplier.s_type == S_Type.CL]
            cleaning_menu = OptionMenu(add_window, cleaning_var, *cleaning_array)
            cleaning_menu.grid(row=8, column=1)

            lbl_decoration = Label(add_window, text="Decoration:")
            lbl_decoration.grid(row=9, column=0, sticky="w")
            decoration_var = tk.StringVar(add_window)
            decoration_var.set("")  # Default value
            decoration_array = [supplier.s_name for supplier in self.suppliers if supplier.s_type == S_Type.D]
            decoration_menu = OptionMenu(add_window, decoration_var, *decoration_array)
            decoration_menu.grid(row=9, column=1)

            lbl_entertainment = Label(add_window, text="Entertainment:")
            lbl_entertainment.grid(row=10, column=0, sticky="w")
            entertainment_var = tk.StringVar(add_window)
            entertainment_var.set("")  # Default value
            entertainment_array = [supplier.s_name for supplier in self.suppliers if supplier.s_type == S_Type.E]
            entertainment_menu = OptionMenu(add_window, entertainment_var, *entertainment_array)
            entertainment_menu.grid(row=10, column=1)

            lbl_furniture = Label(add_window, text="Furniture:")
            lbl_furniture.grid(row=11, column=0, sticky="w")
            furniture_var = tk.StringVar(add_window)
            furniture_var.set("")  # Default value
            furniture_array = [supplier.s_name for supplier in self.suppliers if supplier.s_type == S_Type.F]
            furniture_menu = OptionMenu(add_window, furniture_var, *furniture_array)
            furniture_menu.grid(row=11, column=1)

            lbl_gst_ID = Label(add_window, text="Guest IDs (Seperated by commas):")
            lbl_gst_ID.grid(row=12, column=0, sticky="w")
            entry_gst_ID = Entry(add_window)
            entry_gst_ID.grid(row=12, column=1)






            # Button to save the event details
            btn_save = Button(add_window, text="Save", command=save_event)
            btn_save.grid(row=13, column=0, columnspan=2)

            # Create a notebook for error messages
            error_notebook = ttk.Notebook(add_window)
            error_notebook.grid(row=14, columnspan=2, sticky="ew")
            error_tabs = {}

            # Create tabs for each type of missing detail
            for error_type in ['Client', 'Supplier', 'Venue', 'Guest']:
                error_frame = ttk.Frame(error_notebook)
                error_notebook.add(error_frame, text=error_type)
                error_tabs[error_type] = error_frame

        def delete_event():
            def delete():
                try:
                    e_ID = entry_event_id.get()
                    for event in self.events:
                        if event.e_ID == e_ID:
                            self.events.remove(event)
                            messagebox.showinfo("Success", "Event deleted successfully.")
                            delete_window.destroy()
                            return
                    messagebox.showerror("Error", "Event not found.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid event ID.")

            # Create a new window for deleting event
            delete_window = tk.Toplevel(self.master)
            delete_window.title("Delete Event")

            # Label and entry field for Event ID
            lbl_event_id = tk.Label(delete_window, text="Event ID:")
            lbl_event_id.grid(row=0, column=0, sticky="w")
            entry_event_id = tk.Entry(delete_window)
            entry_event_id.grid(row=0, column=1)

            # Button to delete event
            btn_delete_event = tk.Button(delete_window, text="Delete", command=delete)
            btn_delete_event.grid(row=1, column=0, columnspan=2)

        def modify_event():
            # Define the function to modify an event
            def modify_details(event, detail):
                # Define the function to modify a specific detail of the event
                def save_changes():

                    try:
                        if detail == "Event ID":
                            e_ID = entry_detail.get().strip()
                            if not e_ID.replace(" ", "").isdigit():
                                raise ValueError("ID must contain only numbers.")
                            event.e_ID = e_ID
                        elif detail == "Date":
                            date = entry_detail.get().strip()
                            if not re.match(r"^\d{1,2}-\d{1,2}-\d{4}$", date):
                                raise ValueError("Date must be in the form of DD-MM-YYYY.")
                            event.date = date
                        elif detail == "Time":
                            time = int(entry_detail.get())
                            if not re.match(r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$", time):
                                raise ValueError("Time must be in the form of HH:MM.")
                            event.time = time
                        elif detail == "Duration":
                            duration = entry_detail.get().strip()
                            if not duration.isdigit() or not (1 <= int(duration) <= 10):
                                raise ValueError("Duration must be a number between 1 and 10.")
                            event.duration = duration
                        elif detail == "Guest ID":
                            gst_ID = entry_detail.get().strip()
                            if not re.match(r"^\d+(,\d+)*$", gst_ID):
                                raise ValueError("Guest IDs must be numbers separated by commas.")
                            event.gst_ID = gst_ID

                        messagebox.showinfo("Success", f"Employee {detail} modified successfully.")
                        modify_window.destroy()
                    except ValueError as ve:
                        messagebox.showerror("Error", str(ve))

                    # Create a new window for modifying the selected detail

                modify_window = tk.Toplevel()
                modify_window.title(f"Modify {detail}")

                # Label and entry field for the selected detail
                lbl_detail = tk.Label(modify_window, text=f"{detail}:")
                lbl_detail.grid(row=0, column=0, sticky="w")
                entry_detail = tk.Entry(modify_window)
                entry_detail.grid(row=0, column=1)

                # Set default value in entry field based on the selected detail
                if detail == "ID":
                    entry_detail.insert(0, event.e_ID)
                elif detail == "Date":
                    entry_detail.insert(0, event.date)
                elif detail == "Time":
                    entry_detail.insert(0, event.time)
                elif detail == "Duration":
                    entry_detail.insert(0, event.duration)
                elif detail == "Guest ID":
                    entry_detail.insert(0, event.gst_ID)

                # Button to save the changes
                btn_save = tk.Button(modify_window, text="Save Changes", command=save_changes)
                btn_save.grid(row=1, column=0, columnspan=2)


            def verify_id():
                # Define the function to verify Event ID
                try:
                    # Retrieve the Event ID entered by the user
                    event_id = entry_event_id.get()
                    for event in self.events:
                        if event.e_ID == event_id:
                            # If the ID is correct, show the modify menu
                            modify_window = tk.Toplevel()
                            modify_window.title("Modify Event Details")

                            # Create a menu with different options for modifying event details
                            options = ["Event ID", "Date", "Time", "Duration", "Guest IDs"]
                            for i, option in enumerate(options):
                                btn_option = tk.Button(modify_window, text=option,
                                                       command=lambda o=option: modify_details(event, o))
                                btn_option.grid(row=i, column=0, columnspan=2)

                            return
                    messagebox.showerror("Error", "Event not found.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid event ID.")

            # Create a new window for verifying Event ID
            verify_window = tk.Toplevel(self.master)
            verify_window.title("Verify Event ID")

            # Label and entry field for Event ID
            lbl_id = tk.Label(verify_window, text="Event ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_event_id = tk.Entry(verify_window)
            entry_event_id.grid(row=0, column=1)

            # Button to verify Event ID
            btn_verify = tk.Button(verify_window, text="Verify", command=verify_id)
            btn_verify.grid(row=1, column=0, columnspan=2)

        def display_event():
            # Define the function to display event details
            def display():
                try:
                    # Retrieve the Event ID entered by the user
                    event_id = entry_event_id.get()
                    for event in self.events:
                        if event.e_ID == event_id:
                            # If the event is found, print its details
                            print("Event ID:", event.e_ID)
                            print("Theme:", event.theme)
                            print("Date:", event.date)
                            print("Time:", event.time)
                            print("Duration:", event.duration)
                            print("Venue Address:", event.v_address)
                            print("Client ID:", event.clt_ID)
                            print("Catering:", event.catering)
                            print("Cleaning:", event.cleaning)
                            print("Decoration:", event.decoration)
                            print("Entertainment:", event.entertainment)
                            print("Furniture:", event.furniture)
                            print("Guest IDs:", ", ".join(event.gst_ID))
                            return
                    # If event not found, show an error message
                    messagebox.showerror("Error", "Event not found.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid event ID.")

            # Create a new window for displaying event details
            display_window = tk.Toplevel(self.master)
            display_window.title("Display Event Details")

            # Label and entry field for Event ID
            lbl_id = tk.Label(display_window, text="Event ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_event_id = tk.Entry(display_window)
            entry_event_id.grid(row=0, column=1)

            # Button to display event details
            btn_display = tk.Button(display_window, text="Display", command=display)
            btn_display.grid(row=1, column=0, columnspan=2)

            # It's important to keep a reference to entry_event_id to avoid garbage collection
            display_window.entry_event_id = entry_event_id

        def generate_invoice():
            # Define the function to generate an invoice for the event
            def display_invoice():
                try:
                    # Retrieve the Event ID entered by the user
                    event_id = entry_event_id.get()
                    for event in self.events:
                        if event.e_ID == event_id:
                            # If the event is found, display its invoice
                            invoice_window = tk.Toplevel()
                            invoice_window.title(f"Event {event.e_ID} Invoice")

                            # Calculate and display charges for each service
                            services = {
                                "Venue": 10000,
                                "Catering": 15000,
                                "Cleaning": 7000,
                                "Decoration": 5000,
                                "Entertainment": 11000,
                                "Furniture": 9000
                            }

                            total_charge = 0
                            row = 0
                            for service, charge in services.items():
                                lbl_service = tk.Label(invoice_window, text=f"{service}:")
                                lbl_service.grid(row=row, column=0, sticky="w")
                                lbl_charge = tk.Label(invoice_window, text=f"{charge} AED")
                                lbl_charge.grid(row=row, column=1, sticky="w")
                                total_charge += charge
                                row += 1

                            # Display total charge
                            lbl_total = tk.Label(invoice_window, text=f"Total: {total_charge} AED")
                            lbl_total.grid(row=row, column=0, columnspan=2)

                            return
                    # If event not found, show an error message
                    messagebox.showerror("Error", "Event not found.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid event ID.")

            # Create a new window for generating the invoice
            invoice_window = tk.Toplevel(self.master)
            invoice_window.title("Generate Invoice")

            # Label and entry field for Event ID
            lbl_id = tk.Label(invoice_window, text="Event ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_event_id = tk.Entry(invoice_window)
            entry_event_id.grid(row=0, column=1)

            # Button to display the invoice
            btn_display = tk.Button(invoice_window, text="Display Invoice", command=display_invoice)
            btn_display.grid(row=1, column=0, columnspan=2)

            # It's important to keep a reference to entry_event_id to avoid garbage collection
            invoice_window.entry_event_id = entry_event_id

        event_window = tk.Toplevel(self.master)
        event_window.title("Manage Events")

        btn_add = tk.Button(event_window, text="Add Event", command=add_event)
        if not self.clients:
            messagebox.showerror("Error", "Please create a client first.")
            return
        if not self.suppliers:
            messagebox.showerror("Error", "Please create a supplier first.")
            return
        if not self.venues:
            messagebox.showerror("Error", "Please create a venue first.")
            return
        if not self.guests:
            messagebox.showerror("Error", "Please create a guest first.")
            return
        btn_add.pack()

        btn_delete = tk.Button(event_window, text="Delete Event", command=delete_event)
        btn_delete.pack()

        btn_modify = tk.Button(event_window, text="Modify Event", command=modify_event)
        btn_modify.pack()

        btn_display = tk.Button(event_window, text="Display Event", command=display_event)
        btn_display.pack()

        btn_display = tk.Button(event_window, text="Display Invoice", command=generate_invoice)
        btn_display.pack()


    def manage_employees(self):
        # Implement functionality to manage employees
        def add_new_employee():
            def save_employee():
                try:
                    # Retrieve entered details
                    name = entry_name.get().strip()  # Remove leading and trailing whitespace
                    emp_id = entry_id.get().strip()
                    dept = entry_dept.get().strip()
                    job_title = job_title_var.get()
                    age = int(entry_age.get())
                    dob = entry_dob.get().strip()
                    passport = entry_passport.get().strip()

                    # Check if all details are entered
                    if not (name and emp_id and dept and job_title and dob and passport):
                        messagebox.showerror("Error", "Please enter all details.")
                        return

                    # Check if name contains only letters and spaces
                    if not name.replace(" ", "").isalpha():
                        messagebox.showerror("Error", "Name must contain only letters and spaces.")
                        return

                    # Check if emp_id contains only numbers
                    if not emp_id.isdigit():
                        messagebox.showerror("Error", "Employee ID must contain only numbers.")
                        return

                    # Check if emp_id already exists
                    for emp in self.employees:
                        if emp.emp_ID == emp_id:
                            messagebox.showerror("Error", "Employee ID already exists.")
                            return

                    # Check if dept contains only letters
                    if not dept.isalpha():
                        messagebox.showerror("Error", "Department must contain only letters.")
                        return

                    # Check if age is more than 17 and less than 80
                    if age <= 17 or age >= 80:
                        messagebox.showerror("Error", "Age must be more than 17 and less than 80.")
                        return

                    # Check if dob follows the format 00-00-0000
                    if not re.match(r"\d{2}-\d{2}-\d{4}", dob):
                        messagebox.showerror("Error", "Date of Birth must be in the format DD-MM-YYYY.")
                        return

                    # Check if passport has a length of 8 characters with only letters and numbers
                    if not re.match(r"^[a-zA-Z0-9]{8}$", passport):
                        messagebox.showerror("Error",
                                             "Passport must be 8 characters long and contain only letters and numbers.")
                        return

                    # Create a new employee object
                    new_employee = Employee(name, emp_id, dept, job_title, age, dob, passport)
                    self.employees.append(new_employee)

                    # Close the add window
                    add_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid age.")

            # Create a new window for adding employee details
            add_window = tk.Toplevel(self.master)
            add_window.title("Add New Employee")

            # Define labels and entry fields for employee details
            lbl_name = tk.Label(add_window, text="Name:")
            lbl_name.grid(row=0, column=0, sticky="w")
            entry_name = tk.Entry(add_window)
            entry_name.grid(row=0, column=1)

            lbl_id = tk.Label(add_window, text="Employee ID:")
            lbl_id.grid(row=1, column=0, sticky="w")
            entry_id = tk.Entry(add_window)
            entry_id.grid(row=1, column=1)

            lbl_dept = tk.Label(add_window, text="Department:")
            lbl_dept.grid(row=2, column=0, sticky="w")
            entry_dept = tk.Entry(add_window)
            entry_dept.grid(row=2, column=1)

            lbl_job_title = tk.Label(add_window, text="Job Title:")
            lbl_job_title.grid(row=3, column=0, sticky="w")
            job_titles = [title.value for title in Job_Title]
            job_title_var = tk.StringVar(add_window)
            job_title_var.set(job_titles[0])  # Default value
            dropdown_job_title = tk.OptionMenu(add_window, job_title_var, *job_titles)
            dropdown_job_title.grid(row=3, column=1)

            lbl_age = tk.Label(add_window, text="Age:")
            lbl_age.grid(row=4, column=0, sticky="w")
            entry_age = tk.Entry(add_window)
            entry_age.grid(row=4, column=1)

            lbl_dob = tk.Label(add_window, text="Date of Birth:")
            lbl_dob.grid(row=5, column=0, sticky="w")
            entry_dob = tk.Entry(add_window)
            entry_dob.grid(row=5, column=1)

            lbl_passport = tk.Label(add_window, text="Passport:")
            lbl_passport.grid(row=6, column=0, sticky="w")
            entry_passport = tk.Entry(add_window)
            entry_passport.grid(row=6, column=1)

            # Button to save the employee details
            btn_save = tk.Button(add_window, text="Save", command=save_employee)
            btn_save.grid(row=7, column=0, columnspan=2)

        def delete_employee():
            def delete():
                try:
                    emp_id = entry_id.get()
                    for emp in self.employees:
                        if emp.emp_ID == emp_id:
                            self.employees.remove(emp)
                            messagebox.showinfo("Success", "Employee deleted successfully.")
                            delete_window.destroy()
                            return
                    messagebox.showerror("Error", "Employee not found.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid employee ID.")

            # Create a new window for deleting employee
            delete_window = tk.Toplevel(self.master)
            delete_window.title("Delete Employee")

            # Label and entry field for Employee ID
            lbl_id = tk.Label(delete_window, text="Employee ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_id = tk.Entry(delete_window)
            entry_id.grid(row=0, column=1)

            # Button to delete employee
            btn_delete = tk.Button(delete_window, text="Delete", command=delete)
            btn_delete.grid(row=1, column=0, columnspan=2)

        def modify_employee():
            modify_window = None  # Define modify_window as a global variable

            def modify_details(emp, detail):
                def save_changes():
                    try:
                        if detail == "Name":
                            name = entry_detail.get().strip()
                            if not name.replace(" ", "").isalpha():
                                raise ValueError("Name must contain only letters and spaces.")
                            emp.emp_name = name
                        elif detail == "Department":
                            dept = entry_detail.get().strip()
                            if not dept.isalpha():
                                raise ValueError("Department must contain only letters.")
                            emp.department = dept
                        elif detail == "Age":
                            age = int(entry_detail.get())
                            if age <= 17 or age >= 80:
                                raise ValueError("Age must be between 18 and 79.")
                            emp.age = age
                        elif detail == "Date of Birth":
                            dob = entry_detail.get().strip()
                            if not re.match(r"\d{2}-\d{2}-\d{4}", dob):
                                raise ValueError("Date of Birth must be in the format DD-MM-YYYY.")
                            emp.dob = dob
                        elif detail == "Passport":
                            passport = entry_detail.get().strip()
                            if not re.match(r"^[a-zA-Z0-9]{8}$", passport):
                                raise ValueError(
                                    "Passport must be 8 characters long and contain only letters and numbers.")
                            emp.passport = passport

                        messagebox.showinfo("Success", f"Employee {detail} modified successfully.")
                        modify_window.destroy()
                    except ValueError as ve:
                        messagebox.showerror("Error", str(ve))

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
                    entry_detail.insert(0, emp.emp_name)
                elif detail == "Department":
                    entry_detail.insert(0, emp.department)
                elif detail == "Age":
                    entry_detail.insert(0, emp.age)
                elif detail == "Date of Birth":
                    entry_detail.insert(0, emp.dob)
                elif detail == "Passport":
                    entry_detail.insert(0, emp.passport)

                # Button to save the changes
                btn_save = tk.Button(modify_window, text="Save Changes", command=save_changes)
                btn_save.grid(row=1, column=0, columnspan=2)

            def verify_id():
                try:
                    # Function to verify Employee ID
                    emp_id = entry_id.get()
                    for emp in self.employees:
                        if emp.emp_ID == emp_id:
                            # If ID is correct, show the modify menu
                            nonlocal modify_window
                            modify_window = tk.Toplevel()
                            modify_window.title("Modify Employee Details")

                            # Create a menu with different options for modifying employee details
                            options = ["Name", "Department", "Age", "Date of Birth", "Passport"]
                            for i, option in enumerate(options):
                                btn_option = tk.Button(modify_window, text=option,
                                                       command=lambda o=option: modify_details(emp, o))
                                btn_option.grid(row=i, column=0, columnspan=2)

                            return
                    messagebox.showerror("Error", "Employee not found.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid employee ID.")

            # Create a new window for verifying Employee ID
            verify_window = tk.Toplevel(self.master)
            verify_window.title("Verify Employee ID")

            # Label and entry field for Employee ID
            lbl_id = tk.Label(verify_window, text="Employee ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_id = tk.Entry(verify_window)
            entry_id.grid(row=0, column=1)

            # Button to verify Employee ID
            btn_verify = tk.Button(verify_window, text="Verify", command=verify_id)
            btn_verify.grid(row=1, column=0, columnspan=2)

        def display_employee():
            def display():
                try:
                    emp_id = entry_id.get()
                    for emp in self.employees:
                        if emp.emp_ID == emp_id:
                            emp.display_employee()  # Call the display_employee method of the Employee class
                            return
                    messagebox.showerror("Error", "Employee not found.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid employee ID.")

            # Create a new window for displaying employee details
            display_window = tk.Toplevel(self.master)
            display_window.title("Display Employee Details")

            # Label and entry field for Employee ID
            lbl_id = tk.Label(display_window, text="Employee ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_id = tk.Entry(display_window)
            entry_id.grid(row=0, column=1)

            # Button to display employee details
            btn_display = tk.Button(display_window, text="Display", command=display)
            btn_display.grid(row=1, column=0, columnspan=2)

            # It's important to keep a reference to entry_id to avoid garbage collection
            display_window.entry_id = entry_id

        def assign_manager():
            def assign():
                emp_id = entry_id.get()
                manager_id = entry_manager.get()

                # Find employee and manager objects
                employee = None
                manager = None
                for emp in self.employees:
                    if emp.emp_ID == emp_id:
                        employee = emp
                    if emp.emp_ID == manager_id:
                        manager = emp

                if employee and manager:
                    if employee == manager:
                        messagebox.showerror("Error", "A manager cannot be assigned as the manager for himself.")
                    elif employee.department != manager.department:
                        messagebox.showerror("Error", "Employee and manager must be from the same department.")
                    elif manager.job_title not in [Job_Title.SM, Job_Title.MM]:
                        messagebox.showerror("Error", "Manager must be either a Sales Manager or Marketing Manager.")
                    elif isinstance(employee, Manager):
                        messagebox.showerror("Error", "Employee cannot be assigned as a manager.")
                    else:
                        employee.assign_manager(manager)
                        messagebox.showinfo("Success",
                                            f"{manager.emp_name} assigned as manager to {employee.emp_name}.")
                        assign_window.destroy()
                else:
                    messagebox.showerror("Error", "Employee or manager not found.")

            # Create a new window for assigning manager
            assign_window = tk.Toplevel(self.master)
            assign_window.title("Assign Manager")

            # Label and entry field for Employee ID
            lbl_id = tk.Label(assign_window, text="Employee ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_id = tk.Entry(assign_window)
            entry_id.grid(row=0, column=1)

            # Label and entry field for Manager ID
            lbl_manager = tk.Label(assign_window, text="Manager ID:")
            lbl_manager.grid(row=1, column=0, sticky="w")
            entry_manager = tk.Entry(assign_window)
            entry_manager.grid(row=1, column=1)

            # Button to assign manager
            btn_assign = tk.Button(assign_window, text="Assign", command=assign)
            btn_assign.grid(row=2, column=0, columnspan=2)

        employee_window = tk.Toplevel(self.master)
        employee_window.title("Manage Employees")

        btn_add = tk.Button(employee_window, text="Add Employee", command=add_new_employee)
        btn_add.pack()

        btn_delete = tk.Button(employee_window, text="Delete Employee", command=delete_employee)
        btn_delete.pack()

        btn_modify = tk.Button(employee_window, text="Modify Employee", command=modify_employee)
        btn_modify.pack()

        btn_display = tk.Button(employee_window, text="Display Employee", command=display_employee)
        btn_display.pack()

        btn_display = tk.Button(employee_window, text="Assign Manager", command=assign_manager)
        btn_display.pack()



    def manage_clients(self):
        # Implement functionality to manage clients
        def add_client():
            def save_client():
                try:
                    # Retrieve entered details
                    clt_name = entry_name.get()
                    clt_ID = entry_id.get()
                    clt_address = entry_address.get()
                    clt_contact_details = entry_contact_details.get()
                    budget = entry_budget.get()

                    # Add client with input details
                    new_client = Client().add_client(self.clients, clt_name, clt_ID, clt_address, clt_contact_details,budget)

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

        def delete_client():
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

        def modify_client():
            modify_window = None  # Define modify_window as a global variable

            def modify_details(client, detail):
                def save_changes():
                    try:
                        new_detail = entry_detail.get().strip()

                        if detail == "Name":
                            if not (new_detail.replace(" ", "").isalpha()):
                                raise ValueError("Name must contain only letters and spaces.")
                            client.clt_name = new_detail
                        elif detail == "Address":
                            if not (new_detail.replace(" ", "").isalnum()):
                                raise ValueError("Address must contain only letters, numbers, and spaces.")
                            client.clt_address = new_detail
                        elif detail == "Contact Details":
                            if not re.match(r"^\d{9}$", new_detail):
                                raise ValueError("Contact details must be a phone number with a length of 9 digits.")
                            client.clt_contact_details = new_detail
                        elif detail == "Budget":
                            if not (
                                    new_detail.replace('.', '',
                                                       1).isdigit()):  # Check if it's a valid floating-point number
                                raise ValueError("Budget must be a valid number.")
                            client.budget = float(new_detail)

                        messagebox.showinfo("Success", f"Client {detail} modified successfully.")
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
                    entry_detail.insert(0, client.clt_name)
                elif detail == "Address":
                    entry_detail.insert(0, client.clt_address)
                elif detail == "Contact Details":
                    entry_detail.insert(0, client.clt_contact_details)
                elif detail == "Budget":
                    entry_detail.insert(0, client.budget)

                # Button to save the changes
                btn_save = tk.Button(modify_window, text="Save Changes", command=save_changes)
                btn_save.grid(row=1, column=0, columnspan=2)

            def verify_id():
                try:
                    # Function to verify Client ID
                    clt_ID = entry_id.get()
                    for client in self.clients:
                        if client.clt_ID == clt_ID:
                            # If ID is correct, show the modify menu
                            nonlocal modify_window
                            modify_window = tk.Toplevel()
                            modify_window.title("Modify Client Details")

                            # Create a menu with different options for modifying client details
                            options = ["Name", "Address", "Contact Details", "Budget"]
                            for i, option in enumerate(options):
                                btn_option = tk.Button(modify_window, text=option,
                                                       command=lambda o=option: modify_details(client, o))
                                btn_option.grid(row=i, column=0, columnspan=2)

                            return
                    messagebox.showerror("Error", "Client not found.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid client ID.")

            # Create a new window for verifying Client ID
            verify_window = tk.Toplevel(self.master)
            verify_window.title("Verify Client ID")

            # Label and entry field for Client ID
            lbl_id = tk.Label(verify_window, text="Client ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_id = tk.Entry(verify_window)
            entry_id.grid(row=0, column=1)

            # Button to verify Client ID
            btn_verify = tk.Button(verify_window, text="Verify", command=verify_id)
            btn_verify.grid(row=1, column=0, columnspan=2)

        def display_client():
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

        client_window = tk.Toplevel(self.master)
        client_window.title("Manage Clients")

        btn_add = tk.Button(client_window, text="Add Client", command=add_client)
        btn_add.pack()

        btn_delete = tk.Button(client_window, text="Delete Client", command=delete_client)
        btn_delete.pack()

        btn_modify = tk.Button(client_window, text="Modify Client", command=modify_client)
        btn_modify.pack()

        btn_display = tk.Button(client_window, text="Display Client", command=display_client)
        btn_display.pack()



    def manage_venues(self):
        # Implement functionality to manage venues
        def add_venue():
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

        def delete_venue():
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

        def modify_venue():
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

        def display_venue():
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

        venue_window = tk.Toplevel(self.master)
        venue_window.title("Manage Venues")

        btn_add = tk.Button(venue_window, text="Add Venue", command=add_venue)
        btn_add.pack()

        btn_delete = tk.Button(venue_window, text="Delete Venue", command=delete_venue)
        btn_delete.pack()

        btn_modify = tk.Button(venue_window, text="Modify Venue", command=modify_venue)
        btn_modify.pack()

        btn_display = tk.Button(venue_window, text="Display Venue", command=display_venue)
        btn_display.pack()



    def manage_suppliers(self):
        # Implement functionality to manage suppliers
        def add_supplier():
            def save_supplier():
                s_name = entry_name.get().strip()
                s_ID = entry_id.get().strip()
                s_address = entry_address.get().strip()
                s_contact_details = entry_contact_details.get().strip()
                s_type = S_Type(entry_type_var.get())

                c_min_guests = None  # Initialize with default value
                c_max_guests = None  # Initialize with default value

                if s_type == S_Type.C:  # Check if the selected type is Catering
                    c_min_guests = entry_min_guests.get().strip()  # Get min guests
                    c_max_guests = entry_max_guests.get().strip()  # Get max guests

                    # Check if min and max guests are provided
                    if not (c_min_guests and c_max_guests):
                        messagebox.showerror("Error", "Please enter both minimum and maximum number of guests.")
                        return

                    # Check if min and max guests are numbers
                    if not (c_min_guests.isdigit() and c_max_guests.isdigit()):
                        messagebox.showerror("Error", "Minimum and maximum number of guests must be numbers.")
                        return

                    # Convert guests to integers
                    c_min_guests = int(c_min_guests)
                    c_max_guests = int(c_max_guests)

                    # Check if max guests is greater than min guests
                    if c_max_guests <= c_min_guests:
                        messagebox.showerror("Error",
                                             "Maximum number of guests must be greater than minimum number of guests.")
                        return

                success, message = self.supplier.add_supplier(self.suppliers, s_name, s_ID, s_type, s_address,
                                                              s_contact_details, c_min_guests, c_max_guests)
                if success:
                    add_window.destroy()
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", message)

            add_window = tk.Toplevel(self.master)
            add_window.title("Add New Supplier")

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
            entry_type_var.set(types[0])
            dropdown_type = tk.OptionMenu(add_window, entry_type_var, *types)
            dropdown_type.grid(row=4, column=1)

            # Additional fields for Catering
            lbl_min_guests = tk.Label(add_window, text="Minimum Guests:")  # Label for minimum guests
            lbl_max_guests = tk.Label(add_window, text="Maximum Guests:")  # Label for maximum guests
            entry_min_guests = tk.Entry(add_window)  # Entry field for minimum guests
            entry_max_guests = tk.Entry(add_window)  # Entry field for maximum guests

            # Function to show/hide additional fields based on selected type
            def show_hide_fields(*args):
                if entry_type_var.get() == "Catering":  # If Catering is selected
                    lbl_min_guests.grid(row=5, column=0, sticky="w")
                    lbl_max_guests.grid(row=6, column=0, sticky="w")
                    entry_min_guests.grid(row=5, column=1)
                    entry_max_guests.grid(row=6, column=1)
                else:
                    lbl_min_guests.grid_forget()  # Hide the labels and entry fields
                    lbl_max_guests.grid_forget()
                    entry_min_guests.grid_forget()
                    entry_max_guests.grid_forget()

            entry_type_var.trace("w", show_hide_fields)  # Call the function when dropdown selection changes

            btn_save = tk.Button(add_window, text="Save", command=save_supplier)
            btn_save.grid(row=7, column=0, columnspan=2)

        def delete_supplier():
            def delete():
                s_ID = entry_id.get().strip()
                success, message = self.supplier.delete_supplier(self.suppliers, s_ID)
                if success:
                    delete_window.destroy()
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", message)

            delete_window = tk.Toplevel(self.master)
            delete_window.title("Delete Supplier")

            lbl_id = tk.Label(delete_window, text="Supplier ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_id = tk.Entry(delete_window)
            entry_id.grid(row=0, column=1)

            btn_delete = tk.Button(delete_window, text="Delete", command=delete)
            btn_delete.grid(row=1, column=0, columnspan=2)

        def modify_supplier():
            def modify_details(supplier, detail):
                def save_changes():
                    new_detail = entry_detail.get().strip()
                    success, message = self.supplier.modify_supplier(self.suppliers, supplier.s_ID, detail, new_detail)
                    if success:
                        modify_window.destroy()
                        messagebox.showinfo("Success", message)
                    else:
                        messagebox.showerror("Error", message)

                modify_window = tk.Toplevel()
                modify_window.title(f"Modify {detail}")

                lbl_detail = tk.Label(modify_window, text=f"{detail}:")
                lbl_detail.grid(row=0, column=0, sticky="w")
                entry_detail = tk.Entry(modify_window)
                entry_detail.grid(row=0, column=1)

                if detail == "Name":
                    entry_detail.insert(0, supplier.s_name)
                elif detail == "Address":
                    entry_detail.insert(0, supplier.s_address)
                elif detail == "Contact Details":
                    entry_detail.insert(0, supplier.s_contact_details)

                btn_save = tk.Button(modify_window, text="Save Changes", command=save_changes)
                btn_save.grid(row=1, column=0, columnspan=2)

            def verify_id():
                s_ID = entry_id.get()
                for supplier in self.suppliers:
                    if supplier.s_ID == s_ID:
                        modify_window = tk.Toplevel()
                        modify_window.title("Modify Supplier Details")

                        options = ["Name", "Address", "Contact Details"]
                        for i, option in enumerate(options):
                            btn_option = tk.Button(modify_window, text=option,
                                                   command=lambda o=option: modify_details(supplier, o))
                            btn_option.grid(row=i, column=0, columnspan=2)

                        return
                messagebox.showerror("Error", "Supplier not found.")

            verify_window = tk.Toplevel(self.master)
            verify_window.title("Verify Supplier ID")

            lbl_id = tk.Label(verify_window, text="Supplier ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_id = tk.Entry(verify_window)
            entry_id.grid(row=0, column=1)

            btn_verify = tk.Button(verify_window, text="Verify", command=verify_id)
            btn_verify.grid(row=1, column=0, columnspan=2)

        def display_supplier():
            def display():
                s_ID = entry_id.get().strip()
                success, message = self.supplier.display_supplier(self.suppliers, s_ID)
                if success:
                    messagebox.showinfo("Supplier Details", message)
                else:
                    messagebox.showerror("Error", message)

            display_window = tk.Toplevel(self.master)
            display_window.title("Display Supplier Details")

            lbl_id = tk.Label(display_window, text="Supplier ID:")
            lbl_id.grid(row=0, column=0, sticky="w")
            entry_id = tk.Entry(display_window)
            entry_id.grid(row=0, column=1)

            btn_display = tk.Button(display_window, text="Display", command=display)
            btn_display.grid(row=1, column=0, columnspan=2)

        supplier_window = tk.Toplevel(self.master)
        supplier_window.title("Manage Suppliers")

        btn_add = tk.Button(supplier_window, text="Add Supplier", command=add_supplier)
        btn_add.pack()

        btn_delete = tk.Button(supplier_window, text="Delete Supplier", command=delete_supplier)
        btn_delete.pack()

        btn_modify = tk.Button(supplier_window, text="Modify Supplier", command=modify_supplier)
        btn_modify.pack()

        btn_display = tk.Button(supplier_window, text="Display Supplier", command=display_supplier)
        btn_display.pack()



    def manage_guests(self):
        # Implement functionality to manage guests
        def add_guest():
            def save_guest():
                try:
                    gst_name = entry_name.get()
                    gst_ID = entry_id.get()
                    gst_address = entry_address.get()
                    gst_contact_details = entry_contact_details.get()

                    new_guest = self.guest_management.add_guest(self.guests, gst_name, gst_ID, gst_address,
                                                                gst_contact_details)

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

        def delete_guest():
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

        def modify_guest():
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

        def display_guest():
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

        guest_window = tk.Toplevel(self.master)
        guest_window.title("Manage Guests")

        btn_add = tk.Button(guest_window, text="Add Guest", command=add_guest)
        btn_add.pack()

        btn_delete = tk.Button(guest_window, text="Delete Guest", command=delete_guest)
        btn_delete.pack()

        btn_modify = tk.Button(guest_window, text="Modify Guest", command=modify_guest)
        btn_modify.pack()

        btn_display = tk.Button(guest_window, text="Display Guest", command=display_guest)
        btn_display.pack()

def main():
    root = tk.Tk()
    app = IntegratedSystemGUI(root)
    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root, app))  # Intercept close event
    root.mainloop()

def on_close(root, app):
    app.save_data()  # Save data before exiting
    root.destroy()



# Pickle the instance


if __name__ == "__main__":
    main()



