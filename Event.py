from enum import Enum
from Client import Client
import re
from datetime import datetime
#from System import IntegratedSystemGUI
class Theme(Enum):
  W = "Wedding"
  B = "Birthday"
  T = "Themed Party"
  G = "Graduation"

class Event:
  """Class to represent an Event"""
  def __init__(self, e_ID, theme, date,time, duration, v_address, clt_ID, catering, cleaning, decoration, entertainment, furniture, gst_ID):
    self.e_ID = e_ID
    self.theme = theme
    self.date =  date #Client(clt_ID) if clt_ID is not None else None
    self.time = time
    self.duration = duration
    self.v_address = v_address
    self.clt_ID = clt_ID
    self.catering = catering
    self.cleaning = cleaning
    self.decoration = decoration
    self.entertainment = entertainment
    self.furniture = furniture
    self.gst_ID = gst_ID


  def set_e_ID(self, e_ID):
      self.e_ID = e_ID

  def set_clt_ID(self, clt_ID):
      self.clt_ID = clt_ID
  def set_theme(self, theme):
      self.theme = theme


  def get_e_ID(self):
      return self.e_ID

  def get_clt_ID(self):
      return self.clt_ID

  def get_theme(self):
      return self.theme

  def add_guest(self, guest):
      self.guests.append(guest)


  def add_event(self, events, e_ID, theme, clt_ID,):
      # Validation
      if not (e_ID.isdigit()):
          raise ValueError("Event ID must contain only numbers.")
      if not (clt_ID.isdigit()):
          raise ValueError("Client ID must contain only numbers.")

          # Check if the ID already exists
      for event in events:
          if event.e_ID == e_ID:
              raise ValueError("Event with the same ID already exists.")

      new_event = Event(e_ID, theme,  clt_ID)
      events.append(new_event)
      return new_event

  def delete_event(self, events, e_ID):
      for event in events:
          if event.e_ID == e_ID:
                  events.remove(event)
                  return True
          return False

  def modify_event(self, events, e_ID, theme=None,  client=None):
      for event in events:
          if event.e_ID == e_ID:
              if theme is not None:
                  event.theme = theme
              if client is not None:
                  event.client = client
                  return True
          return False

  def display_event(self, events, e_ID):
      for event in events:
          if event.e_ID == e_ID:
              return event
          return None
