from enum import Enum  # Import Enum module for creating enumerated constants

class Job_Title(Enum):
    """Enum class to represent job titles"""
    SM = "Sales Manager"
    S = "Salesperson"
    MM = "Marketing Manager"
    MK = "Marketer"
    A = "Accountant"
    D = "Designer"
    H = "Handyman"

class Employee:
    """Class to represent an employee"""

    def __init__(self, emp_name='', emp_ID=0, department='', job_title=None, age=0, dob="", passport=""):
        self.emp_name = emp_name  # Initialize employee name
        self.emp_ID = emp_ID  # Initialize employee ID
        self.department = department  # Initialize employee department
        self.job_title = Job_Title(job_title) if job_title is not None else None  # Ensure job_title is an Enum value
        self.b_salary = self.basic_salary(self.job_title)  # Pass job_title to basic_salary method
        self.age = age  # Initialize employee age
        self.dob = dob  # Initialize employee date of birth
        self.passport = passport  # Initialize employee passport
        self.manager = None  # Initialize manager as None

    def basic_salary(self, job_title):
        """Method to calculate basic salary based on job title"""
        salaries = {
            Job_Title.SM: 37000,
            Job_Title.S: 20000,
            Job_Title.MM: 40000,
            Job_Title.MK: 25000,
            Job_Title.A: 21000,
            Job_Title.D: 19000,
            Job_Title.H: 15000
        }
        return salaries.get(job_title, 0)  # Get salary corresponding to the job title, default to 0 if not found

    def assign_manager(self, manager):
        """Method to assign a manager to an employee"""
        pass  # Placeholder method for assigning manager

    def display_employee(self):
        """Method to display employee information"""
        manager_info = ""  # Initialize manager information string
        if self.manager:
            manager_info = (f"\nManager ID: {self.manager.emp_ID}\nManager Name: {self.manager.emp_name}")  # Get manager information if exists

        print(f"Name: {self.emp_name}\nEmployee ID: {self.emp_ID}\nDepartment: {self.department}\nJob Title: {self.job_title.value}\nSalary: {self.b_salary}\nAge: {self.age}\nDate of Birth: {self.dob}\nPassport: {self.passport}{manager_info}")  # Print employee details

class Manager(Employee):
    """Class to represent a manager"""

    def __init__(self, emp_name='', emp_ID=0, department='', job_title=None, age=0, dob="", passport=""):
        super().__init__(emp_name, emp_ID, department, job_title, age, dob, passport)  # Initialize attributes using parent class constructor
        self.m_employees = []  # Initialize manager's employees list

    def add_employee(self, employee):
        """Method to add an employee to manager's list"""
        self.m_employees.append(employee)  # Add employee to manager's list


