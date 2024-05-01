from enum import Enum

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

  def add_event(self, events, e_ID, theme, date, time, duration, v_address,clt_ID,guests, catering,cleaning, decoration, entertainment, furniture):
