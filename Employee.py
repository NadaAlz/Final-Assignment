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
        self.job_title = job_title
        self.b_salary = self.basic_salary(job_title)
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

    def assign_manager(self, manager):
        if isinstance(manager, Manager) and manager.department == self.department:
            if isinstance(self, Manager):
                print(self.emp_name, "is already a manager")
            else:
                self.manager = manager
                print(manager.emp_name, "is", self.emp_name, "Manager")
        else:
            print("Invalid manager assignment.")


class Manager(Employee):
    def __init__(self, emp_name='', emp_ID='', department='', job_title=None, age=0, dob="", passport=""):
        super().__init__(emp_name, emp_ID, department, job_title, age, dob, passport)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


employees = []  # Global list to store employees


def add_new_employee():
    def save_employee():
        try:
            # Retrieve entered details
            name = entry_name.get().strip()  # Remove leading and trailing whitespace
            emp_id = entry_id.get().strip()
            dept = entry_dept.get().strip()
            job_title = job_title_var.get()
            age = int(entry_age.get())
            dob = entry_dob.get()
            passport = entry_passport.get()

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

            # Check if age is more than 17
            if age <= 17 and age>=80:
                messagebox.showerror("Error", "Age must be more than 17 and less than 80.")
                return

            # Check if emp_id already exists
            for emp in employees:
                if emp.emp_ID == emp_id:
                    messagebox.showerror("Error", "Employee with the same ID already exists.")
                    return

            # Create a new employee object
            new_employee = Employee(name, emp_id, dept, job_title, age, dob, passport)
            employees.append(new_employee)

            # Close the add window
            add_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age.")

    # Create a new window for adding employee details
    add_window = tk.Toplevel()
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


def delete_employee():
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
    delete_window = tk.Toplevel()
    delete_window.title("Delete Employee")

    # Label and entry field for Employee ID
    lbl_id = tk.Label(delete_window, text="Employee ID:")
    lbl_id.grid(row=0, column=0, sticky="w")
    entry_id = tk.Entry(delete_window)
    entry_id.grid(row=0, column=1)

    # Button to delete employee
    btn_delete = tk.Button(delete_window, text="Delete", command=delete)
    btn_delete.grid(row=1, column=0, columnspan=2)


def modify_employee():
    modify_window = None  # Define modify_window as a global variable

    def modify_details(emp, entry_name, entry_dept, job_title_var, entry_age, entry_dob, entry_passport):
        try:
            # Function to modify employee details
            emp.emp_name = entry_name.get()
            emp.department = entry_dept.get()
            emp.job_title = job_title_var.get()  # Directly set the job title without using enumeration
            emp.age = int(entry_age.get())
            emp.dob = entry_dob.get()
            emp.passport = entry_passport.get()
            messagebox.showinfo("Success", "Employee details modified successfully.")
            modify_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age.")

    def verify_id():
        try:
            # Define job_titles here or pass it as an argument to verify_id() if it's defined elsewhere
            job_titles = [title.value for title in Job_Title]

            # Function to verify Employee ID
            emp_id = entry_id.get()
            for emp in employees:
                if emp.emp_ID == emp_id:
                    # If ID is correct, show the modify menu
                    nonlocal modify_window
                    modify_window = tk.Toplevel()
                    modify_window.title("Modify Employee Details")

                    # Label and entry fields for modified details
                    lbl_name = tk.Label(modify_window, text="Name:")
                    lbl_name.grid(row=0, column=0, sticky="w")
                    entry_name = tk.Entry(modify_window)
                    entry_name.grid(row=0, column=1)

                    lbl_dept = tk.Label(modify_window, text="Department:")
                    lbl_dept.grid(row=1, column=0, sticky="w")
                    entry_dept = tk.Entry(modify_window)
                    entry_dept.grid(row=1, column=1)

                    lbl_job_title = tk.Label(modify_window, text="Job Title:")
                    lbl_job_title.grid(row=2, column=0, sticky="w")
                    job_title_var = tk.StringVar(modify_window)
                    job_title_var.set(job_titles[0])  # Default value
                    dropdown_job_title = tk.OptionMenu(modify_window, job_title_var, *job_titles)
                    dropdown_job_title.grid(row=2, column=1)

                    lbl_age = tk.Label(modify_window, text="Age:")
                    lbl_age.grid(row=3, column=0, sticky="w")
                    entry_age = tk.Entry(modify_window)
                    entry_age.grid(row=3, column=1)

                    lbl_dob = tk.Label(modify_window, text="Date of Birth:")
                    lbl_dob.grid(row=4, column=0, sticky="w")
                    entry_dob = tk.Entry(modify_window)
                    entry_dob.grid(row=4, column=1)

                    lbl_passport = tk.Label(modify_window, text="Passport:")
                    lbl_passport.grid(row=5, column=0, sticky="w")
                    entry_passport = tk.Entry(modify_window)
                    entry_passport.grid(row=5, column=1)

                    # Button to modify employee details
                    btn_modify = tk.Button(modify_window, text="Modify",
                                           command=lambda: modify_details(emp, entry_name, entry_dept, job_title_var,
                                                                          entry_age, entry_dob, entry_passport))
                    btn_modify.grid(row=6, column=0, columnspan=2)
                    return
            messagebox.showerror("Error", "Employee not found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid employee ID.")

    # Create a new window for verifying Employee ID
    verify_window = tk.Toplevel()
    verify_window.title("Verify Employee ID")

    # Label and entry field for Employee ID
    lbl_id = tk.Label(verify_window, text="Employee ID:")
    lbl_id.grid(row=0, column=0, sticky="w")
    entry_id = tk.Entry(verify_window)
    entry_id.grid(row=0, column=1)

    # Button to verify Employee ID
    btn_verify = tk.Button(verify_window, text="Verify", command=verify_id)
    btn_verify.grid(row=1, column=0, columnspan=2)


def display_employee(root):
    def display():
        try:
            emp_id = entry_id.get()
            for emp in employees:
                if emp.emp_ID == emp_id:
                    messagebox.showinfo("Employee Details",
                                        f"Name: {emp.emp_name}\nEmployee ID: {emp.emp_ID}\nDepartment: {emp.department}\nJob Title: {emp.job_title.value}\nAge: {emp.age}\nDate of Birth: {emp.dob}\nPassport: {emp.passport}")
                    return
            messagebox.showerror("Error", "Employee not found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid employee ID.")

    # Create a new window for displaying employee details
    display_window = tk.Toplevel(root)  # Pass root as the master
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


# Update the button in main() to pass the root as an argument
def assign_manager():
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
            if employee.department != manager.department:
                messagebox.showerror("Error", "Employee and manager must be from the same department.")
            elif isinstance(employee, Manager):
                messagebox.showerror("Error", "Employee cannot be a manager.")
            else:
                employee.assign_manager(manager)
                messagebox.showinfo("Success", f"{manager.emp_name} assigned as manager to {employee.emp_name}.")
                assign_window.destroy()
        else:
            messagebox.showerror("Error", "Employee or manager not found.")

    # Create a new window for assigning manager
    assign_window = tk.Toplevel()
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
    root.title("Employee Management System")

    btn_add_new = tk.Button(root, text="Add New Employee Details", command=add_new_employee)
    btn_add_new.pack()

    btn_delete = tk.Button(root, text="Delete Employee Details", command=delete_employee)
    btn_delete.pack()

    btn_modify = tk.Button(root, text="Modify Details", command=modify_employee)
    btn_modify.pack()

    btn_display = tk.Button(root, text="Display Employee Details", command=lambda: display_employee(root))
    btn_display.pack()

    btn_assign_manager = tk.Button(root, text="Assign Manager", command=assign_manager)
    btn_assign_manager.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
