import tkinter as tk
from tkinter import messagebox
from enum import Enum
import re

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

    def __init__(self, emp_name='', emp_ID='', department='', job_title=None, age=0, dob="", passport=""):
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
    def __init__(self, emp_name='', emp_ID='', department='', job_title=None, age=0, dob="", passport=""):
        super().__init__(emp_name, emp_ID, department, job_title, age, dob, passport)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class EmployeeManagementGUI:
    def __init__(self, master):
        self.master = master
        master.title("Employee Management System")

        self.btn_add_new = tk.Button(master, text="Add New Employee Details", command=self.add_new_employee)
        self.btn_add_new.pack()

        self.btn_delete = tk.Button(master, text="Delete Employee Details", command=self.delete_employee)
        self.btn_delete.pack()

        self.btn_modify = tk.Button(master, text="Modify Details", command=self.modify_employee)
        self.btn_modify.pack()

        self.btn_display = tk.Button(master, text="Display Employee Details", command=self.display_employee)
        self.btn_display.pack()

        self.btn_assign_manager = tk.Button(master, text="Assign Manager", command=self.assign_manager)
        self.btn_assign_manager.pack()

    def add_new_employee(self):
        def save_employee():
            try:
                # Retrieve entered details
                name = entry_name.get().strip()  # Remove leading and trailing whitespace
                emp_id = entry_id.get().strip()
                dept = entry_dept.get().strip()
                job_title = job_title_var.get()
                age = int(entry_age.get())
                dob = entry_dob.get().strip()
                passport = entry_passport.get().strip()

                # Check if all details are entered
                if not (name and emp_id and dept and job_title and dob and passport):
                    messagebox.showerror("Error", "Please enter all details.")
                    return

                # Check if name contains only letters and spaces
                if not name.replace(" ", "").isalpha():
                    messagebox.showerror("Error", "Name must contain only letters and spaces.")
                    return

                # Check if emp_id contains only numbers
                if not emp_id.isdigit():
                    messagebox.showerror("Error", "Employee ID must contain only numbers.")
                    return

                # Check if dept contains only letters
                if not dept.isalpha():
                    messagebox.showerror("Error", "Department must contain only letters.")
                    return

                # Check if age is more than 17 and less than 80
                if age <= 17 and age >= 80:
                    messagebox.showerror("Error", "Age must be more than 17 and less than 80.")
                    return

                # Check if dob follows the format 00-00-0000
                if not re.match(r"\d{2}-\d{2}-\d{4}", dob):
                    messagebox.showerror("Error", "Date of Birth must be in the format DD-MM-YYYY.")
                    return

                # Check if passport has a length of 8 characters with only letters and numbers
                if not re.match(r"^[a-zA-Z0-9]{8}$", passport):
                    messagebox.showerror("Error", "Passport must be 8 characters long and contain only letters and numbers.")
                    return

                # Create a new employee object
                new_employee = Employee(name, emp_id, dept, job_title, age, dob, passport)
                employees.append(new_employee)

                # Close the add window
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid age.")

        # Create a new window for adding employee details
        add_window = tk.Toplevel(self.master)
        add_window.title("Add New Employee")

        # Define labels and entry fields for employee details
        lbl_name = tk.Label(add_window, text="Name:")
        lbl_name.grid(row=0, column=0, sticky="w")
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1)

        lbl_id = tk.Label(add_window, text="Employee ID:")
        lbl_id.grid(row=1, column=0, sticky="w")
        entry_id = tk.Entry(add_window)
        entry_id.grid(row=1, column=1)

        lbl_dept = tk.Label(add_window, text="Department:")
        lbl_dept.grid(row=2, column=0, sticky="w")
        entry_dept = tk.Entry(add_window)
        entry_dept.grid(row=2, column=1)

        lbl_job_title = tk.Label(add_window, text="Job Title:")
        lbl_job_title.grid(row=3, column=0, sticky="w")
        job_titles = [title.value for title in Job_Title]
        job_title_var = tk.StringVar(add_window)
        job_title_var.set(job_titles[0])  # Default value
        dropdown_job_title = tk.OptionMenu(add_window, job_title_var, *job_titles)
        dropdown_job_title.grid(row=3, column=1)

        lbl_age = tk.Label(add_window, text="Age:")
        lbl_age.grid(row=4, column=0, sticky="w")
        entry_age = tk.Entry(add_window)
        entry_age.grid(row=4, column=1)

        lbl_dob = tk.Label(add_window, text="Date of Birth:")
        lbl_dob.grid(row=5, column=0, sticky="w")
        entry_dob = tk.Entry(add_window)
        entry_dob.grid(row=5, column=1)

        lbl_passport = tk.Label(add_window, text="Passport:")
        lbl_passport.grid(row=6, column=0, sticky="w")
        entry_passport = tk.Entry(add_window)
        entry_passport.grid(row=6, column=1)

        # Button to save the employee details
        btn_save = tk.Button(add_window, text="Save", command=save_employee)
        btn_save.grid(row=7, column=0, columnspan=2)

    def delete_employee(self):
        def delete():
            try:
                emp_id = entry_id.get()
                for emp in employees:
                    if emp.emp_ID == emp_id:
                        employees.remove(emp)
                        messagebox.showinfo("Success", "Employee deleted successfully.")
                        delete_window.destroy()
                        return
                messagebox.showerror("Error", "Employee not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid employee ID.")

        # Create a new window for deleting employee
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Employee")

        # Label and entry field for Employee ID
        lbl_id = tk.Label(delete_window, text="Employee ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(delete_window)
        entry_id.grid(row=0, column=1)

        # Button to delete employee
        btn_delete = tk.Button(delete_window, text="Delete", command=delete)
        btn_delete.grid(row=1, column=0, columnspan=2)

    def modify_employee(self):
        modify_window = None  # Define modify_window as a global variable

        def modify_details(emp, detail):
            def save_changes():
                try:
                    if detail == "Name":
                        emp.emp_name = entry_detail.get()
                    elif detail == "Department":
                        emp.department = entry_detail.get()
                    elif detail == "Age":
                        emp.age = int(entry_detail.get())
                    elif detail == "Date of Birth":
                        emp.dob = entry_detail.get()
                    elif detail == "Passport":
                        emp.passport = entry_detail.get()

                    messagebox.showinfo("Success", f"Employee {detail} modified successfully.")
                    modify_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid value.")

            # Create a new window for modifying the selected detail
            modify_window = tk.Toplevel()
            modify_window.title(f"Modify {detail}")

            # Label and entry field for the selected detail
            lbl_detail = tk.Label(modify_window, text=f"{detail}:")
            lbl_detail.grid(row=0, column=0, sticky="w")
            entry_detail = tk.Entry(modify_window)
            entry_detail.grid(row=0, column=1)

            # Set default value in entry field based on the selected detail
            if detail == "Name":
                entry_detail.insert(0, emp.emp_name)
            elif detail == "Department":
                entry_detail.insert(0, emp.department)
            elif detail == "Age":
                entry_detail.insert(0, emp.age)
            elif detail == "Date of Birth":
                entry_detail.insert(0, emp.dob)
            elif detail == "Passport":
                entry_detail.insert(0, emp.passport)

            # Button to save the changes
            btn_save = tk.Button(modify_window, text="Save Changes", command=save_changes)
            btn_save.grid(row=1, column=0, columnspan=2)

        def verify_id():
            try:
                # Function to verify Employee ID
                emp_id = entry_id.get()
                for emp in employees:
                    if emp.emp_ID == emp_id:
                        # If ID is correct, show the modify menu
                        nonlocal modify_window
                        modify_window = tk.Toplevel()
                        modify_window.title("Modify Employee Details")

                        # Create a menu with different options for modifying employee details
                        options = ["Name", "Department", "Age", "Date of Birth", "Passport"]
                        for i, option in enumerate(options):
                            btn_option = tk.Button(modify_window, text=option,
                                                   command=lambda o=option: modify_details(emp, o))
                            btn_option.grid(row=i, column=0, columnspan=2)

                        return
                messagebox.showerror("Error", "Employee not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid employee ID.")

        # Create a new window for verifying Employee ID
        verify_window = tk.Toplevel(self.master)
        verify_window.title("Verify Employee ID")

        # Label and entry field for Employee ID
        lbl_id = tk.Label(verify_window, text="Employee ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(verify_window)
        entry_id.grid(row=0, column=1)

        # Button to verify Employee ID
        btn_verify = tk.Button(verify_window, text="Verify", command=verify_id)
        btn_verify.grid(row=1, column=0, columnspan=2)

    def display_employee(self):
        def display():
            try:
                emp_id = entry_id.get()
                for emp in employees:
                    if emp.emp_ID == emp_id:
                        emp.display_employee()  # Call the display_employee method of the Employee class
                        return
                messagebox.showerror("Error", "Employee not found.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid employee ID.")

        # Create a new window for displaying employee details
        display_window = tk.Toplevel(self.master)
        display_window.title("Display Employee Details")

        # Label and entry field for Employee ID
        lbl_id = tk.Label(display_window, text="Employee ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(display_window)
        entry_id.grid(row=0, column=1)

        # Button to display employee details
        btn_display = tk.Button(display_window, text="Display", command=display)
        btn_display.grid(row=1, column=0, columnspan=2)

        # It's important to keep a reference to entry_id to avoid garbage collection
        display_window.entry_id = entry_id

    def assign_manager(self):
        def assign():
            emp_id = entry_id.get()
            manager_id = entry_manager.get()

            # Find employee and manager objects
            employee = None
            manager = None
            for emp in employees:
                if emp.emp_ID == emp_id:
                    employee = emp
                if emp.emp_ID == manager_id:
                    manager = emp

            if employee and manager:
                if employee == manager:
                    messagebox.showerror("Error", "A manager cannot be assigned as the manager for himself.")
                elif employee.department != manager.department:
                    messagebox.showerror("Error", "Employee and manager must be from the same department.")
                elif manager.job_title not in [Job_Title.SM, Job_Title.MM]:
                    messagebox.showerror("Error", "Manager must be either a Sales Manager or Marketing Manager.")
                elif isinstance(employee, Manager):
                    messagebox.showerror("Error", "Employee cannot be assigned as a manager.")
                else:
                    employee.assign_manager(manager)
                    messagebox.showinfo("Success", f"{manager.emp_name} assigned as manager to {employee.emp_name}.")
                    assign_window.destroy()
            else:
                messagebox.showerror("Error", "Employee or manager not found.")

        # Create a new window for assigning manager
        assign_window = tk.Toplevel(self.master)
        assign_window.title("Assign Manager")

        # Label and entry field for Employee ID
        lbl_id = tk.Label(assign_window, text="Employee ID:")
        lbl_id.grid(row=0, column=0, sticky="w")
        entry_id = tk.Entry(assign_window)
        entry_id.grid(row=0, column=1)

        # Label and entry field for Manager ID
        lbl_manager = tk.Label(assign_window, text="Manager ID:")
        lbl_manager.grid(row=1, column=0, sticky="w")
        entry_manager = tk.Entry(assign_window)
        entry_manager.grid(row=1, column=1)

        # Button to assign manager
        btn_assign = tk.Button(assign_window, text="Assign", command=assign)
        btn_assign.grid(row=2, column=0, columnspan=2)


def main():
    root = tk.Tk()
    app = EmployeeManagementGUI(root)
    root.mainloop()

#if __name__ == "__main__":
 #   employees = []  # Global list to store employees
  #  main()