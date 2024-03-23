from datetime import datetime

class Employee:
    def __init__(self, id, first_name, last_name, year_joined):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.year_joined = int(year_joined)

    def displaySalary(self):
        pass

class FixedSalaryEmployee(Employee):
    def __init__(self, id, first_name, last_name, year_joined, basic_salary):
        super().__init__(id, first_name, last_name, year_joined)
        self.basic_salary = basic_salary

    def displaySalary(self):
        years = datetime.now().year - self.year_joined
        if years < 2:
            additional_percentage = 0
        elif 2 <= years <= 5:
            additional_percentage = 0.05
        else:
            additional_percentage = 0.10
        return self.basic_salary * (1 + additional_percentage)

class CommissionEmployee(Employee):
    def __init__(self, id, first_name, last_name, year_joined, minimum_salary, num_clients, amount_per_client):
        super().__init__(id, first_name, last_name, year_joined)
        self.minimum_salary = minimum_salary
        self.num_clients = num_clients
        self.amount_per_client = amount_per_client

    def displaySalary(self):
        return max(self.minimum_salary, self.num_clients * self.amount_per_client)

def employeeWithMostClients(employees):
    max_clients = 0
    max_employee = None
    for employee in employees:
        if isinstance(employee, CommissionEmployee) and employee.num_clients > max_clients:
            max_clients = employee.num_clients
            max_employee = employee
    return max_employee
