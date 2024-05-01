from enum import Enum
import re
from datetime import datetime

class Theme(Enum):
  W = "Wedding"
  B = "Birthday"
  T = "Themed Party"
  G = "Graduation"

class Event:
  """Class to represent an Event"""
  def __init__(self, e_ID='', theme=Theme.W, date='', time='', duration=0.0, v_address='', clt_ID='', guests=[], catering=None, cleaning=None, decoration=None, entertainment=None, furniture=None, invoice=None):
    self.e_ID = e_ID
    self.theme = theme
    self.date = date
    self.time = time
    self.duration = duration
    self.v_address = v_address
    self.clt_ID = clt_ID
    self.guests = guests
    self.catering = catering
    self.cleaning = cleaning
    self.decoration = decoration
    self.entertainment = entertainment
    self.furniture = furniture
    self.invoice = invoice

  def set_e_ID(self, e_ID):
      self.e_ID = e_ID

  def set_theme(self, theme):
      self.theme = theme

  def set_date(self, date):
      self.date = date

  def set_time(self, time):
      self.time = time

  def set_duration(self, duration):
      self.duration = duration

  def get_e_ID(self):
      return self.e_ID

  def get_theme(self):
      return self.theme

  def get_date(self):
      return self.date

  def get_time(self):
      return self.time

  def get_duration(self):
      return self.duration

  def add_event(self, events, e_ID, theme, date, time, duration, v_address, clt_ID, guests, catering, cleaning,
                decoration, entertainment, furniture):
      # 1. Check if e_ID consists only of numbers
      if not e_ID.isdigit():
          raise ValueError("Event ID must contain only numbers.")

      # 2. Validate that theme is one of the choices available in the GUI
      if theme not in [t.value for t in Theme]:
          raise ValueError("Invalid theme choice.")

      # 3. Ensure date is in the format "DD-MM-YYYY"
      try:
          datetime.strptime(date, "%d-%m-%Y")
      except ValueError:
          raise ValueError("Invalid date format. Use DD-MM-YYYY.")

      # 4. Validate time to ensure it consists of either numbers or characters
      if not re.match(r'^[\d\w]+$', time):
          raise ValueError("Invalid time format. Use numbers or characters.")

      # 5. Check if duration is a number between 1 and 10
      if not duration.isdigit() or not (1 <= int(duration) <= 10):
          raise ValueError("Duration must be a number between 1 and 10.")

      # 6. Verify if v_address exists in the system (assuming v_address is the venue address)
      if v_address not in [venue.v_address for venue in self.venues]:
          raise ValueError("Venue address does not exist in the system.")

      # 7. Check if clt_ID is valid (assuming clt_ID is the client ID)
      if clt_ID not in [client.clt_ID for client in self.clients]:
          raise ValueError("Client ID is not valid.")

      # 8. Validate guests using gst_ID
      for gst_ID in guests:
          if gst_ID not in [guest.gst_ID for guest in self.guests]:
              raise ValueError(f"Guest with ID {gst_ID} does not exist in the system.")

      # 9. Validate other services (catering, cleaning, decoration, entertainment, and furniture) using s_ID
      for service in [catering, cleaning, decoration, entertainment, furniture]:
          if service:
              if service.s_ID not in [supplier.s_ID for supplier in self.suppliers]:
                  raise ValueError(f"Service with ID {service.s_ID} does not exist in the system.")

      # After all validations pass, create the event
      new_event = Event(e_ID, theme, date, time, duration, v_address, clt_ID, guests, catering, cleaning, decoration,
                        entertainment, furniture)
      events.append(new_event)
      return new_event

  def delete_event(self, events, e_ID):
      # Find the event with the provided e_ID
      for event in events:
          if event.e_ID == e_ID:
              events.remove(event)
              return True  # Event found and deleted

      # If the event with the provided e_ID is not found
      return False  # Event not found

  def modify_event(self, events, e_ID, theme, date, time, duration, v_address, clt_ID, guests, catering, cleaning,
                   decoration, entertainment, furniture):
      # Validate inputs
      try:
          # Check if e_ID contains only numbers
          if not e_ID.isdigit():
              raise ValueError("Event ID must contain only numbers.")

          # Check if theme is one of the choices in the GUI
          if theme not in [t.value for t in Theme]:
              raise ValueError("Invalid theme choice.")

          # Check if date is in the form of DD-MM-YYYY
          if not re.match(r"\d{2}-\d{2}-\d{4}", date):
              raise ValueError("Invalid date format. Use DD-MM-YYYY.")

          # Check if duration is a number from 1 to 10
          duration = float(duration)
          if not (1 <= duration <= 10):
              raise ValueError("Duration must be a number from 1 to 10.")

          # Check if v_address exists in the system
          # (Assuming Venue objects are stored in self.venues)
          if v_address not in [venue.v_address for venue in self.venues]:
              raise ValueError("Venue address does not exist in the system.")

          # Check if clt_ID exists in the system
          # (Assuming Client objects are stored in self.clients)
          if clt_ID not in [client.clt_ID for client in self.clients]:
              raise ValueError("Client ID does not exist in the system.")

          # Validate guests using gst_ID
          for guest_id in guests:
              if guest_id not in [guest.gst_ID for guest in self.guests]:
                  raise ValueError(f"Guest with ID {guest_id} does not exist.")

          # Validate catering, cleaning, decoration, entertainment, furniture using s_Id
          for service_id in [catering, cleaning, decoration, entertainment, furniture]:
              if service_id:
                  if service_id not in [supplier.s_ID for supplier in self.suppliers]:
                      raise ValueError(f"Supplier with ID {service_id} does not exist.")
      except ValueError as e:
          # If any validation fails, raise an error with the specific message
          raise ValueError(f"Validation error: {str(e)}")

      # Find the event with the provided e_ID
      for event in events:
          if event.e_ID == e_ID:
              # Modify the event attributes
              event.theme = theme
              event.date = date
              event.time = time
              event.duration = duration
              event.v_address = v_address
              event.clt_ID = clt_ID
              event.guests = guests
              event.catering = catering
              event.cleaning = cleaning
              event.decoration = decoration
              event.entertainment = entertainment
              event.furniture = furniture
              return True  # Event modified

      # If the event with the provided e_ID is not found
      return False  # Event not found

  def display_event(self, events, e_ID):
      # Find the event with the provided e_ID
      for event in events:
          if event.e_ID == e_ID:
              # Construct a string with event details
              event_details = (
                  f"Event ID: {event.e_ID}\n"
                  f"Theme: {event.theme}\n"
                  f"Date: {event.date}\n"
                  f"Time: {event.time}\n"
                  f"Duration: {event.duration}\n"
                  f"Venue Address: {event.v_address}\n"
                  f"Client ID: {event.clt_ID}\n"
                  f"Guests: {', '.join(event.guests)}\n"
                  f"Catering Supplier ID: {event.catering}\n"
                  f"Cleaning Supplier ID: {event.cleaning}\n"
                  f"Decoration Supplier ID: {event.decoration}\n"
                  f"Entertainment Supplier ID: {event.entertainment}\n"
                  f"Furniture Supplier ID: {event.furniture}\n"
              )
              return event_details  # Return event details as a string

      # If the event with the provided e_ID is not found
      return "Event not found."  # Return a message indicating event not found
