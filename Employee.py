from enum import Enum
class Job_Title(Enum):
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
        self.emp_name = emp_name
        self.emp_ID = emp_ID
        self.department = department
        self.job_title = Job_Title(job_title) if job_title is not None else None  # Ensure job_title is an Enum value
        self.b_salary = self.basic_salary(self.job_title)  # Pass job_title to basic_salary method
        self.age = age
        self.dob = dob
        self.passport = passport
        self.manager = None

    def basic_salary(self, job_title):
        salaries = {
            Job_Title.SM: 37000,
            Job_Title.S: 20000,
            Job_Title.MM: 40000,
            Job_Title.MK: 25000,
            Job_Title.A: 21000,
            Job_Title.D: 19000,
            Job_Title.H: 15000
        }
        return salaries.get(job_title, 0)

    def assign_manager(self,manager):
        pass

    def display_employee(self):
        manager_info = ""
        if self.manager:
            manager_info = (f"\nManager ID: {self.manager.emp_ID}\nManager Name: {self.manager.emp_name}")

        print(f"Name: {self.emp_name}\nEmployee ID: {self.emp_ID}\nDepartment: {self.department}\nJob Title: {self.job_title.value}\nSalary: {self.b_salary}\nAge: {self.age}\nDate of Birth: {self.dob}\nPassport: {self.passport}{manager_info}")


class Manager(Employee):
    def __init__(self, emp_name='', emp_ID=0, department='', job_title=None, age=0, dob="", passport=""):
        super().__init__(emp_name, emp_ID, department, job_title, age, dob, passport)
        self.m_employees = []

    def add_employee(self, employee):
        self.m_employees.append(employee)

