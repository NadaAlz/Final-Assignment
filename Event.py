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
  def __init__(self, e_ID='', theme=Theme.W, client=None):
    self.e_ID = e_ID
    self.theme = theme
    self.client = Client(client) if client is not None else None

  def set_e_ID(self, e_ID):
      self.e_ID = e_ID

  def set_client(self, client):
      self.client = client
  def set_theme(self, theme):
      self.theme = theme


  def get_e_ID(self):
      return self.e_ID

  def get_client(self):
      return self.client

  def get_theme(self):
      return self.theme


  def add_event(self, events, e_ID, theme, client,):
      # Validation
      if not (e_ID.isdigit()):
          raise ValueError("Event ID must contain only numbers.")
      if not (client.isdigit()):
          raise ValueError("Client ID must contain only numbers.")

          # Check if the ID already exists
      for event in events:
          if event.e_ID == e_ID:
              raise ValueError("Event with the same ID already exists.")

      new_event = Event(e_ID, theme,  client)
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
