import sys
from typing import List
from Entities import Department, Employee
from Enumerates import Positions, Growth
from datetime import date

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


if __name__ == "__main__":
    Director = Employee('John', Positions.Director, 300000, date(2000, 9, 1))
    company_1 = Department('BIG_COMPANY', Director)

    pr1 = Employee('Jack', Positions.Programmer, 150000, date(2003, 8, 2))
    dep1 = Department('Department_1', pr1)
    empl1 = Employee('Ann', Positions.Secreter, 70000, date(2003, 9, 9))
    dep1.hire(empl1)
    company_1.add_department(dep1)

    pr2 = Employee('Mary', Positions.Programmer, 150000, date(2004, 10, 12))
    dep2 = Department('Department_2', pr2)
    empl2 = Employee('Jane', Positions.Secreter, 80000, date(2006, 12, 4))
    dep2.hire(empl2)
    company_1.add_department(dep2)

    Director2 = Employee('Sasha', Positions.Director, 2000000, date(2008, 12, 9))
    company_2 = Department('small_COMPANY', Director)
    
    pr1 = Employee('Tom', Positions.Secreter, 190000, date(2009, 2, 1))
    dep1 = Department('Department_1', pr1)
    company_2.add_department(dep1)  
    
    empl2.change_position(Positions.Secreter, Growth.PROMOTED) 
    
    assert company_1 >= company_2
    assert company_2 <= company_1
    assert company_1 != company_2
    assert company_1 == company_2
