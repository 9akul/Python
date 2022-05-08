import sys
from typing import List
from Entities import Department, Employee
from Enumerates import Positions, Growth
from datetime import date
from abc import abstractmethod

class Activities:

    @abstractmethod
    def by_position(department: Department, position: Positions) -> List[Employee]:
        pass

    @abstractmethod
    def by_salary(department: Department, begin: int, end: int) -> List[Employee]:
        pass

class Activity(Activities):

def by_position(department: Department, position: Positions) -> List[Employee]:
    result: List[Employee] = []

    for i in department.employees:
        if i.position == position:
            result.append(i)

    for j in department.department:
        result.extend(by_position(j, position))

    return result

def by_salary(department: Department, begin: int, end: int) -> List[Employee]:
    result: List[Employee] = []
    if begin is None:
        begin = 0

    if end is None:
        end = sys.maxsize

    for i in department.employees:
        if begin <= i.salary <= end:
            result.append(i)

    for j in department.department:
        result.extend(by_salary(j, begin, end))

    return result
