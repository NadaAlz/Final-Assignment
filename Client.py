import re  # Import regular expression module for pattern matching

class Client:
    """Class to represent a client"""
    def __init__(self, clt_name='', clt_ID=0, clt_address='', clt_contact_details='', budget=0.0):
        self.clt_name = clt_name  # Initialize client's name
        self.clt_ID = clt_ID  # Initialize client's ID
        self.clt_address = clt_address  # Initialize client's address
        self.clt_contact_details = clt_contact_details  # Initialize client's contact details
        self.budget = budget  # Initialize client's budget

    def set_clt_name(self, clt_name):
        self.clt_name = clt_name  # Set client's name

    def set_clt_ID(self, clt_ID):
        self.clt_ID = clt_ID  # Set client's ID

    def set_clt_address(self, clt_address):
        self.clt_address = clt_address  # Set client's address

    def set_clt_contact_details(self, clt_contact_details):
        self.clt_contact_details = clt_contact_details  # Set client's contact details

    def set_budget(self, budget):
        self.budget = budget  # Set client's budget

    def get_clt_name(self):
        return self.clt_name  # Get client's name

    def get_clt_ID(self):
        return self.clt_ID  # Get client's ID

    def get_clt_address(self):
        return self.clt_address  # Get client's address

    def get_clt_contact_details(self):
        return self.clt_contact_details  # Get client's contact details

    def get_budget(self):
        return self.budget  # Get client's budget

    def add_client(self, clients, clt_name, clt_ID, clt_address, clt_contact_details, budget):
        # Validation
        if not (clt_name.strip().replace(" ", "").isalpha()):
            raise ValueError("Name must contain only letters and spaces.")
        if not (clt_ID.isdigit()):
            raise ValueError("Client ID must contain only numbers.")
        if not (clt_address.strip().replace(" ", "").isalnum()):
            raise ValueError("Address must contain only letters, numbers, and spaces.")
        if not re.match(r"^\d{9}$", clt_contact_details):
            raise ValueError("Contact details must be a phone number with a length of 9 digits.")
        if not (budget.replace('.', '', 1).isdigit()):  # Check if it's a valid floating-point number
            raise ValueError("Budget must be a valid number.")

        # Check if the ID already exists
        for client in clients:
            if client.clt_ID == clt_ID:
                raise ValueError("Client with the same ID already exists.")

        new_client = Client(clt_name, clt_ID, clt_address, clt_contact_details, float(budget))  # Create a new client
        clients.append(new_client)  # Add the new client to the list of clients
        return new_client

    def delete_client(self, clients, clt_ID):
        for client in clients:
            if client.clt_ID == clt_ID:
                clients.remove(client)  # Delete the client
                return True
        return False

    def modify_client(self, clients, clt_ID, clt_name=None, clt_address=None, clt_contact_details=None, budget=None):
        for client in clients:
            if client.clt_ID == clt_ID:
                if clt_name is not None:
                    client.clt_name = clt_name  # Modify client's name if provided
                if clt_address is not None:
                    client.clt_address = clt_address  # Modify client's address if provided
                if clt_contact_details is not None:
                    client.clt_contact_details = clt_contact_details  # Modify client's contact details if provided
                if budget is not None:
                    client.budget = float(budget)  # Modify client's budget if provided
                return True
        return False

    def display_client(self, clients, clt_ID):
        for client in clients:
            if client.clt_ID == clt_ID:
                return client  # Return the client with the provided ID
        return None  # Return None if client not found


