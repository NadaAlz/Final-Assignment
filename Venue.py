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



