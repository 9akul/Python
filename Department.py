from .Activities import Activities
from .Employees import Position, Employee
from typing import List

class Department:

    def __init__(self, name, boss: Employee):
        self.boss = boss
        self.name = name
        self.departments = []
        self.employees = []
        self.hire(boss)

    def add_department(self, department):
        self.departments.append(department)

    @property
    def department(self):
        return self.departments

    @property
    def employees(self) -> List[Employee]:
        return self.employees

    @property
    def all_workers(self) -> List[Employee]:
        result = self.employees
        depart = self.departments
        while len(depart) > 0:
            d = depart.pop()
            result.extend(d.employees)
            depart.extend(d.department)
        return result

    def hire(self, employee: Employee):
        self.employees.append(employee)
        employee.department = self

    def change_salary(self, is_percent: bool, salary_amount: int):
        for i in self.employees:
            if i.active:
                i.salary = i.salary * (1 + salary_amount / 100) if is_percent else i.salary + salary_amount

    def __check_class(func):
        def wrapper(one, two):
            if not isinstance(two, Department):
                return None
            return func(one, two)
        return wrapper

    @__check_class
    def __lt__(self, other):
        return len(self.all_workers) < len(other.all_workers)    

    @__check_class
    def __gt__(self, other):
        return  len(self.all_workers) > len(other.all_workers)

    @__check_class
    def __ge__(self, other):
        return len(self.all_workers) >= len(other.all_workers)

    @__check_class
    def __le__(self, other):
        return len(self.all_workers) <= len(other.all_workers)

    @__check_class
    def __eq__(self, other):
        return len(self.all_workers) == len(other.all_workers)

    @__check_class
    def __ne__(self, other):
        return len(self.all_workers) != len(other.all_workers)

    @__check_class
    def __sub__(self, other):
        return True

    @__check_class
    def __or__(self, other):
        return True

    @__check_class
    def __and__(self, other):
        return True
