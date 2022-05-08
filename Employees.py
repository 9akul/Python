from abc import abstractmethod
from enum import Enum
from datetime import date

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
