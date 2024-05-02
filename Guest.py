import re  # Import regular expression module for pattern matching

class Guest:
    """Class to represent a guest"""
    def __init__(self, gst_name='', gst_ID=0, gst_address='', gst_contact_details=''):
        self.gst_name = gst_name  # Initialize guest's name
        self.gst_ID = gst_ID  # Initialize guest's ID
        self.gst_address = gst_address  # Initialize guest's address
        self.gst_contact_details = gst_contact_details  # Initialize guest's contact details

    def set_gst_name(self, gst_name):
        self.gst_name = gst_name  # Set guest's name

    def set_gst_ID(self, gst_ID):
        self.gst_ID = gst_ID  # Set guest's ID

    def set_gst_address(self, gst_address):
        self.gst_address = gst_address  # Set guest's address

    def set_gst_contact_details(self, gst_contact_details):
        self.gst_contact_details = gst_contact_details  # Set guest's contact details

    def get_gst_name(self):
        return self.gst_name  # Get guest's name

    def get_gst_ID(self):
        return self.gst_ID  # Get guest's ID

    def get_gst_address(self):
        return self.gst_address  # Get guest's address

    def get_gst_contact_details(self):
        return self.gst_contact_details  # Get guest's contact details

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

        new_guest = Guest(gst_name, gst_ID, gst_address, gst_contact_details)  # Create a new guest
        guests.append(new_guest)  # Add the new guest to the list of guests
        return new_guest

    def delete_guest(self, guests, gst_ID):
        for guest in guests:
            if guest.gst_ID == gst_ID:
                guests.remove(guest)  # Delete the guest
                return True
        return False

    def modify_guest(self, guests, gst_ID, gst_name=None, gst_address=None, gst_contact_details=None):
        for guest in guests:
            if guest.gst_ID == gst_ID:
                if gst_name is not None:
                    guest.gst_name = gst_name  # Modify guest's name if provided
                if gst_address is not None:
                    guest.gst_address = gst_address  # Modify guest's address if provided
                if gst_contact_details is not None:
                    guest.gst_contact_details = gst_contact_details  # Modify guest's contact details if provided
                return True
        return False

    def display_guest(self, guests, gst_ID):
        for guest in guests:
            if guest.gst_ID == gst_ID:
                return guest  # Return the guest with the provided ID
        return None  # Return None if guest not found







