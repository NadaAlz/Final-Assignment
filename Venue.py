import re  # Import regular expression module for pattern matching

class Venue:
    """Class to represent a venue"""

    def __init__(self, v_name='', v_ID=0, v_address='', v_contact='', v_min_guests=0, v_max_guests=0):
        self.v_name = v_name  # Initialize venue name
        self.v_ID = v_ID  # Initialize venue ID
        self.v_address = v_address  # Initialize venue address
        self.v_contact = v_contact  # Initialize venue contact
        self.v_min_guests = v_min_guests  # Initialize venue minimum guests
        self.v_max_guests = v_max_guests  # Initialize venue maximum guests

    def set_v_name(self, v_name):
        self.v_name = v_name  # Set venue name

    def set_v_ID(self, v_ID):
        self.v_ID = v_ID  # Set venue ID

    def set_v_address(self, v_address):
        self.v_address = v_address  # Set venue address

    def set_v_contact(self, v_contact):
        self.v_contact = v_contact  # Set venue contact

    def set_v_min_guests(self, v_min_guests):
        self.v_min_guests = v_min_guests  # Set venue minimum guests

    def set_v_max_guests(self, v_max_guests):
        self.v_max_guests = v_max_guests  # Set venue maximum guests

    def get_v_name(self):
        return self.v_name  # Get venue name

    def get_v_ID(self):
        return self.v_ID  # Get venue ID

    def get_v_address(self):
        return self.v_address  # Get venue address

    def get_v_contact(self):
        return self.v_contact  # Get venue contact

    def get_v_min_guests(self):
        return self.v_min_guests  # Get venue minimum guests

    def get_v_max_guests(self):
        return self.v_max_guests  # Get venue maximum guests

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

        new_venue = Venue(v_name, v_ID, v_address, v_contact, int(v_min_guests), int(v_max_guests))  # Create a new venue
        venues.append(new_venue)  # Add the new venue to the list of venues
        return new_venue

    def delete_venue(self, venues, v_ID):
        for venue in venues:
            if venue.v_ID == v_ID:
                venues.remove(venue)  # Delete the venue
                return True
        return False

    def modify_venue(self, venues, v_ID, v_name=None, v_address=None, v_contact=None, v_min_guests=None,
                     v_max_guests=None):
        for venue in venues:
            if venue.v_ID == v_ID:
                if v_name is not None:
                    venue.v_name = v_name  # Modify venue's name if provided
                if v_address is not None:
                    venue.v_address = v_address  # Modify venue's address if provided
                if v_contact is not None:
                    venue.v_contact = v_contact  # Modify venue's contact if provided
                if v_min_guests is not None:
                    venue.v_min_guests = int(v_min_guests)  # Modify venue's minimum guests if provided
                if v_max_guests is not None:
                    venue.v_max_guests = int(v_max_guests)  # Modify venue's maximum guests if provided
                return True
        return False

    def display_venue(self, venues, v_ID):
        for venue in venues:
            if venue.v_ID == v_ID:
                return venue  # Return the venue with the provided ID
        return None  # Return None if venue not found
