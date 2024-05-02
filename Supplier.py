from enum import Enum
import re

class S_Type(Enum):
    """Class to represent supplier type as Enum values"""
    C = "Catering"
    CL = "Cleaning"
    F = "Furniture"
    D = "Decorations"
    E = "Entertainment"

class Supplier:
    """Class to represent a supplier"""
    #Constructor to initialize attributes:
    def __init__(self, s_name='', s_ID=0, s_type=S_Type.C, s_address='', s_contact_details=''):
        self.s_name = s_name
        self.s_ID = s_ID
        self.s_type = s_type
        self.s_address = s_address
        self.s_contact_details = s_contact_details

    #Setter Functions
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

    #Getter Functions
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

    #Function to create a new supplier
    def add_supplier(self, suppliers, s_name, s_ID, s_type, s_address, s_contact_details, c_min_guests=None,
                     c_max_guests=None):
        try:
            # Check if all details are provided
            if not (s_name and s_ID and s_address and s_contact_details):
                raise ValueError("Please enter all details.")

            # Check if the ID already exists
            for supplier in suppliers:
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

            if s_type == S_Type.C:  # Additional checks for Catering type
                # Check if both min and max guests are provided
                if c_min_guests is None or c_max_guests is None:
                    raise ValueError("Please enter both minimum and maximum number of guests.")

                # Convert guests to integers
                c_min_guests = int(c_min_guests)
                c_max_guests = int(c_max_guests)

                # Check if min and max guests are numbers
                if not (str(c_min_guests).isdigit() and str(c_max_guests).isdigit()):
                    raise ValueError("Minimum and maximum number of guests must be numbers.")

                # Check if max guests is greater than min guests
                if c_max_guests <= c_min_guests:
                    raise ValueError("Maximum number of guests must be greater than minimum number of guests.")

            # Add supplier with input details
            new_supplier = Supplier(s_name, s_ID, s_type, s_address, s_contact_details)
            suppliers.append(new_supplier)

            return True, "Supplier added successfully."
        except ValueError as e:
            return False, str(e)

   #Function to delete a supplier given an ID
    def delete_supplier(self, suppliers, s_ID):
        try:
            #This checks each supplier in the suppliers' list and deletes the desired supplier
            for supplier in suppliers:
                if supplier.s_ID == s_ID:
                    suppliers.remove(supplier)
                    return True, "Supplier deleted successfully."
            return False, "Supplier not found."
        except ValueError:
            return False, "Please enter a valid supplier ID."

    #Function to modify a supplier details given the ID and the chosen detail and the new detail
    def modify_supplier(self, suppliers, s_ID, detail, new_detail):
        try:
            for supplier in suppliers:
                if supplier.s_ID == s_ID:
                    #These lines will check what the user wants to modify and then change the detail to the given one
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

                    #The details are changed
                    return True, f"Supplier {detail} modified successfully."
            #The supplier with this ID does not exist
            return False, "Supplier not found."
        except ValueError as e:
            return False, str(e)

    #Function to display a supplier details given the ID
    def display_supplier(self, suppliers, s_ID):
        try:
            for supplier in suppliers:
                if supplier.s_ID == s_ID:
                    #This will go through each detail and print it
                    details = f"Name: {supplier.s_name}\nID: {supplier.s_ID}\nType: {supplier.s_type.value}\n" \
                              f"Address: {supplier.s_address}\nContact Details: {supplier.s_contact_details}"
                    return True, details
            return False, "Supplier not found."
        except ValueError:
            return False, "Please enter a valid supplier ID."

class Catering_Company(Supplier):
    """Class to represent a catering company as a child of Supplier Class """

    #Constructor
    def __init__(self, s_name='', s_ID=0, s_type=S_Type.C, s_address='', s_contact_details='', menu=[], c_min_guests=0, c_max_guests=0):
        super().__init__(s_name, s_ID, s_type, s_address, s_contact_details) #Inheritance
        self.menu = menu
        self.c_min_guests = c_min_guests
        self.c_max_guests = c_max_guests

   #Setter Functions

    def set_menu(self, menu):
        self.menu = menu

    def set_c_min_guests(self, c_min_guests):
        self.c_min_guests = c_min_guests

    def set_c_max_guests(self, c_max_guests):
        self.c_max_guests = c_max_guests

    #Getter Functions
    def get_menu(self):
        return self.menu

    def get_c_min_guests(self):
        return self.c_min_guests

    def get_c_max_guests(self):
        return self.c_max_guests

