from typing import List
from datetime import date
from Enumerates import Positions, Growth

class Change:
    def __init__(self, init_date: date, position: Position, growth: Growth):
        self.init_date = init_date
        self.position = position
        self.growth = growth

class Employees:
    def __init__(self, name: str, position: Position, salary: int, date: date):
        self.name = name
        self.position = position
        self.salary = salary
        self.date = date
        self.active = True
        self.department = None
        self.growth = []
        self.add_growth_list(position, Growth.HIRED)

    @property
    def position(self) -> Position:
        return self.position

    @property
    def department(self):
        return self.department

    @department.setter
    def department(self, depart):
        self.department = depart

    def change_position(self, new_position: Position, growth: Growth):
        self.add_growth_list(new_position, growth)
        self.position = new_position
        if growth is Growth.FIRED:
            self.active = False

    @property
    def history(self) -> List[Change]:
        return self.growth

    def fire(self):
        self.active = False

    def add_growth_list(self, new_position: Position, growth: Growth):
        if growth is Growth.HIRED:
            history = Change(self.date, new_position, growth, self.name, ' was ', growth.value)
        else:
            history = Change(date.today(), new_position, growth, self.name,' was ', growth.value + (' from ', self.position.value, 'to ', new_position.value if new_position is not None else ''))
        self.growth.append(history)


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
