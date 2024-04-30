class Guest:
  """Class to represent a guest"""
  def __init__(self, gst_name='', gst_ID='', gst_address='', gst_contact_details=''):
    self.gst_name = gst_name
    self.gst_ID = gst_ID
    self.gst_address = gst_address
    self.gst_contact_details = gst_contact_details

  def set_gst_name(self, gst_name):
      self.gst_name = gst_name

  def set_gst_ID(self, gst_ID):
      self.gst_ID = gst_ID

  def set_gst_address(self, gst_address):
      self.gst_address = gst_address

  def set_gst_contact_details(self, gst_contact_details):
      self.gst_contact_details = gst_contact_details


  def get_gst_name(self):
      return self.gst_name

  def get_gst_ID(self):
      return self.gst_ID

  def get_gst_address(self):
      return self.gst_address

  def get_gst_contact_details(self):
      return self.gst_contact_details

