class Employee:
    employees = {}  # Class-level dictionary to store employee instances

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        Employee.employees[emp_id] = self  # Add employee instance to the dictionary

    def display_details(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")

    @classmethod
    def get_employee_by_id(cls, emp_id):
        return cls.employees.get(emp_id)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")


class Developer(Employee):
    def __init__(self, emp_id, name, salary, languages):
        super().__init__(emp_id, name, salary)
        self.languages = languages

    def display_details(self):
        super().display_details()
        print(f"Languages: {', '.join(self.languages)}")


# Create employee instances
manager1 = Manager(101, "Rajeeve", 80000, 5)
manager2 = Manager(102, "Imran", 70000, 12)
developer1 = Developer(201, "Spandana", 22000, ["Python", "Automation"])
developer2 = Developer(202, "Alice Johnson", 24000, ["JAVA", "JavaScript"])

# Get employee ID from user
try:
    employee_id = int(input("Enter Employee ID: "))
    employee = Employee.get_employee_by_id(employee_id)

    if employee:
        print("Employee Details:")
        employee.display_details()
    else:
        print(f"Employee with ID {employee_id} not found.")
except ValueError:
    print("Invalid input. Please enter a valid Employee ID (a number).")
