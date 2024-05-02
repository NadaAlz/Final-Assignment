from enum import Enum  # Import Enum module for creating enumerated constants


class Theme(Enum):
    """Class to represent Theme as Enum values"""
    W = "Wedding"  # Wedding theme
    B = "Birthday"  # Birthday theme
    T = "Themed Party"  # Themed Party theme
    G = "Graduation"  # Graduation theme


class Event:
    """Class to represent an Event"""

    # Constructor
    def __init__(self, e_ID, theme, date, time, duration, v_address, clt_ID, catering, cleaning, decoration,
                 entertainment, furniture, gst_ID):
        self.e_ID = e_ID  # Event ID
        self.theme = theme  # Event theme
        self.date = date  # Event date
        self.time = time  # Event time
        self.duration = duration  # Event duration
        self.v_address = v_address  # Venue address (Association with Venye class)
        self.clt_ID = clt_ID  # Client ID
        self.catering = catering  # Catering service (Association with Supplier class)
        self.cleaning = cleaning  # Cleaning service (Association with Supplier class)
        self.decoration = decoration  # Decoration service (Association with Supplier class)
        self.entertainment = entertainment  # Entertainment service (Association with Supplier class)
        self.furniture = furniture  # Furniture service (Association with Supplier class)
        self.gst_ID = gst_ID  # Guest ID

    # Setter Functions
    def set_e_ID(self, e_ID):
        self.e_ID = e_ID  # Set Event ID

    def set_clt_ID(self, clt_ID):
        self.clt_ID = clt_ID  # Set Client ID

    def set_theme(self, theme):
        self.theme = theme  # Set Event theme

    # Getter Functions
    def get_e_ID(self):
        return self.e_ID  # Get Event ID

    def get_clt_ID(self):
        return self.clt_ID  # Get Client ID

    def get_theme(self):
        return self.theme  # Get Event theme

    def add_guest(self, guest):
        self.guests.append(guest)  # Add guest to the event

    def add_event(self, events, e_ID, theme, clt_ID):
        # Validation
        if not (e_ID.isdigit()):
            raise ValueError("Event ID must contain only numbers.")
        if not (clt_ID.isdigit()):
            raise ValueError("Client ID must contain only numbers.")

        # Check if the ID already exists
        for event in events:
            if event.e_ID == e_ID:
                raise ValueError("Event with the same ID already exists.")

        new_event = Event(e_ID, theme, clt_ID)  # Create a new event
        events.append(new_event)  # Add the new event to the list of events
        return new_event

   #Function to delete an event by providing the ID
    def delete_event(self, events, e_ID):
        for event in events:
            if event.e_ID == e_ID:
                events.remove(event)  # Delete the event
                return True
        return False

    # Function to modify an event by providing the ID
    def modify_event(self, events, e_ID, theme=None, client=None):
        for event in events:
            if event.e_ID == e_ID:
                if theme is not None:
                    event.theme = theme  # Modify event theme if provided
                if client is not None:
                    event.client = client  # Modify client if provided
                    return True
        return False

    # Function to display an event by providing the ID
    def display_event(self, events, e_ID):
        for event in events:
            if event.e_ID == e_ID:
                return event  # Return the event with the provided ID
        return None  # Return None if event not found
